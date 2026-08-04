#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert the OSW HTML guides into GitBook-ready markdown pages.

The HTML files are the source of truth. Re-run this after editing them:

    python tools/html-to-gitbook.py v4.html
    python tools/html-to-gitbook.py v4.html --only a1,a2     # pilot subset

The left sidebar in the HTML already carries the exact tree we want in
GitBook, so the nav drives the split:

    div.grp   -> '## Group' heading in SUMMARY.md   (bold, not clickable)
    a.flow    -> flow page       (A1)
    a.st      -> step page       (A1.1, A1.x)       nested under the flow
    a.st2     -> sub-step page   (A1.x.1)           nested under the step

Every page is written flat at the repo root so image links stay relative to
the screenshots that already live there.
"""
import argparse
import os
import re
import sys

from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

EMPHASIS = {'b': '**', 'strong': '**', 'i': '*', 'em': '*', 'code': '`'}


def slugify(text: str) -> str:
    text = text.lower().replace('&', ' and ')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def clean(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


# --------------------------------------------------------------------------
# inline / block rendering
# --------------------------------------------------------------------------

def inline(node, anchors: dict) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ''

    inner = ''.join(inline(c, anchors) for c in node.children)

    if node.name in EMPHASIS:
        body = inner.strip()
        if not body:
            return ''
        mark = EMPHASIS[node.name]
        return f'{mark}{body}{mark}'
    if node.name == 'a':
        href = node.get('href', '')
        if href.startswith('#'):
            href = anchors.get(href[1:], href)
        elif not href and node.get('data-goto'):
            href = anchors.get(node['data-goto'], '')  # cross-flow jump in the HTML
        return f'[{inner.strip()}]({href})' if href else inner
    if node.name == 'br':
        return '\n'
    return inner


def render_table(table: Tag, anchors: dict) -> str:
    rows = []
    for tr in table.find_all('tr'):
        cells = [clean(inline(td, anchors)) for td in tr.find_all(['th', 'td'])]
        if cells:
            rows.append(cells)
    if not rows:
        return ''
    width = max(len(r) for r in rows)
    rows = [r + [''] * (width - len(r)) for r in rows]
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * width]
    out += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
    return '\n'.join(out)


def render_figure(fig: Tag, anchors: dict, indent: str = '') -> str:
    img = fig.find('img')
    if not img:
        return ''
    out = [f'{indent}![{clean(img.get("alt", ""))}]({img.get("src", "")})']
    cap = fig.find('figcaption')
    if cap:
        # Captions are already italic: drop inner bold so we don't emit '***x***',
        # then escape stray asterisks ('Roles*') that would close the italics early.
        text = clean(inline(cap, anchors)).replace('**', '').replace('*', r'\*')
        if text:
            out.append(f'{indent}*{text}*')
    return '\n\n'.join(out)


def split_item(el: Tag, anchors: dict) -> tuple[str, list]:
    """Split a <li> into its own text and the blocks (figures/tables) inside it."""
    blocks, text_parts = [], []
    for child in el.children:
        # a wrapper div only counts as a block if it actually wraps one
        if isinstance(child, Tag) and child.name == 'div' and 'call' in (child.get('class') or []):
            blocks.append(('callout', child))
            continue
        if isinstance(child, Tag) and child.name == 'div' and child.find(['table', 'figure']):
            child = child.find(['table', 'figure'])
        if isinstance(child, Tag) and child.name in ('figure', 'table', 'ol', 'ul'):
            if child.name == 'figure':
                blocks.append(('figure', child))
            elif child.name == 'table':
                blocks.append(('table', child))
            else:
                blocks.append(('list', child))
        else:
            text_parts.append(inline(child, anchors))
    return clean(''.join(text_parts)), blocks


def render_callout(div: Tag, anchors: dict, indent: str = '') -> str:
    """A .call box becomes a blockquote, so its title stops running into its body."""
    title_el = div.find('span', class_='t')
    title = clean(inline(title_el, anchors)) if title_el else ''
    # rebuild the body without the title, rather than extracting it from the soup
    body = clean(''.join(inline(c, anchors) for c in div.children if c is not title_el))
    lines = []
    if title:
        lines.append(f'**{title}**')
        if body:
            lines.append('')
    if body:
        lines.append(body)
    return '\n'.join(f'{indent}> {l}'.rstrip() for l in lines)


def render_blocks(blocks: list, anchors: dict, indent: str = '') -> list:
    out = []
    for kind, node in blocks:
        if kind == 'figure':
            out.append(render_figure(node, anchors, indent))
        elif kind == 'callout':
            out.append(render_callout(node, anchors, indent))
        elif kind == 'table':
            table = render_table(node, anchors)
            out.append('\n'.join(indent + l for l in table.splitlines()) if indent else table)
        else:
            for sub in node.find_all('li', recursive=False):
                out.append(f'{indent}- ' + clean(inline(sub, anchors)))
    return [b for b in out if b]


def split_lead(text: str) -> tuple[str, str]:
    """'**Click + Create New** (top-right) → …' -> ('Click + Create New', '(top-right) → …')."""
    if text.startswith('**'):
        end = text.find('**', 2)
        if end > 2:
            # lstrip only: the rest keeps its own closing punctuation
            return text[2:end].strip(' .:—-'), text[end + 2:].lstrip(' .:—-')
    return '', text


def render_steps(ol: Tag, anchors: dict, skip_ids: set, as_headings: bool = False) -> list:
    """Steps of a flow.

    as_headings turns each step into an H2 so it shows up in GitBook's
    "On this page" outline, which only lists H1 and H2.
    """
    lines, number = [], 0
    for li in ol.find_all('li', recursive=False):
        if li.get('id') in skip_ids:
            continue
        number += 1
        text, blocks = split_item(li, anchors)
        code = li.get('data-code')

        if as_headings:
            lead, rest = split_lead(text)
            heading = ' · '.join(x for x in (code, lead) if x) or f'Step {number}'
            lines.append(f'## {heading}')
            if rest:
                lines.append(rest)
            elif not lead:
                lines.append(text)
            lines += render_blocks(blocks, anchors)
        else:
            lines.append(f'{number}. **{code}** — {text}' if code else f'{number}. {text}')
            lines += render_blocks(blocks, anchors, indent='   ')
    return lines


def render_flow_elements(elements: list, anchors: dict, skip_ids: set,
                         as_headings: bool = False) -> list:
    lines = []
    for el in elements:
        classes = el.get('class') or []
        if el.name == 'nav' or any(c.startswith('pagernav') for c in classes):
            continue  # prev/next pager belongs to the HTML layout
        if el.name == 'ol':
            lines += render_steps(el, anchors, skip_ids, as_headings)
        elif el.name == 'ul':
            for li in el.find_all('li', recursive=False):
                text, blocks = split_item(li, anchors)
                lines.append(f'* {text}')
                lines += render_blocks(blocks, anchors, indent='  ')
        elif el.name == 'table':
            lines.append(render_table(el, anchors))
        elif el.name == 'figure':
            lines.append(render_figure(el, anchors))
        elif el.name == 'div' and 'call' in classes:
            lines.append(render_callout(el, anchors))
        elif el.name == 'div' and el.find(['table', 'figure', 'ol', 'ul']):
            # wrappers like <div class="tblwrap"><table>…</table></div>
            lines += render_flow_elements(el.find_all(recursive=False), anchors, skip_ids)
        elif el.name in ('p', 'div', 'h4'):
            text = clean(inline(el, anchors))
            if text:
                lines.append(f'## {text}' if el.name == 'h4' else text)
    return lines


# --------------------------------------------------------------------------
# nav -> page tree
# --------------------------------------------------------------------------

class Page:
    def __init__(self, title: str, filename: str, anchor: str = '', page_id: str = ''):
        self.title = title
        self.filename = filename
        self.anchor = anchor        # id of the h3 / li this page came from
        self.page_id = page_id      # 'page-a1'
        self.children: list[Page] = []
        # A nav entry pointing at an anchor another entry already owns. It stays
        # in the sidebar as a cross-reference and links to that page instead of
        # getting a duplicate of its own.
        self.alias = False


def parse_nav(soup: BeautifulSoup) -> list:
    """Return [(group_title, [flow Page, ...]), ...] mirroring the HTML sidebar."""
    nav = soup.find('nav')
    groups, flow, step = [], None, None
    seen = {}                       # anchor -> the file that owns it

    aliases = []                    # resolved after the walk, the owner may come later

    def make(title, el, page_id):
        anchor = el.get('href', '#')[1:]
        # class="xref" marks a sidebar entry that only points at another entry's
        # section. It never owns a page, whichever order the two appear in.
        if 'xref' in (el.get('class') or []) or anchor in seen:
            p = Page(title, '', anchor=anchor, page_id=page_id)
            p.alias = True
            aliases.append(p)
            return p
        p = Page(title, slugify(title) + '.md', anchor=anchor, page_id=page_id)
        seen[anchor] = p.filename
        return p

    for el in nav.find_all(['div', 'a']):
        classes = el.get('class') or []
        if 'grp' in classes:
            groups.append((clean(el.get_text()), []))
            flow = step = None
        elif 'flow' in classes:
            title = clean(el.get_text())
            code = clean(el.find(class_='n').get_text()) if el.find(class_='n') else ''
            if code:
                title = f'{code} · {clean(title[len(code):])}'
            flow = Page(title, slugify(title) + '.md', page_id=el.get('data-page', ''))
            if not groups:
                groups.append(('Guide', []))
            groups[-1][1].append(flow)
            step = None
        elif 'st2' in classes and step is not None:
            step.children.append(make(clean(el.get_text()), el, step.page_id))
        elif 'st' in classes and flow is not None:
            step = make(clean(el.get_text()), el, flow.page_id)
            flow.children.append(step)

    for p in aliases:
        p.filename = seen.get(p.anchor, '')
        if not p.filename:
            print(f'  !! cross-reference #{p.anchor} has no page', file=sys.stderr)

    return groups


def build_anchor_map(groups: list) -> dict:
    """Every HTML anchor id -> the markdown file that now holds it."""
    anchors = {}
    for _, flows in groups:
        for flow in flows:
            anchors[flow.page_id] = flow.filename  # data-goto="page-inbox" jumps
            for step in flow.children:
                anchors.setdefault(step.anchor, step.filename)
                for sub in step.children:
                    anchors.setdefault(sub.anchor, sub.filename)
    return anchors


# --------------------------------------------------------------------------
# page writing
# --------------------------------------------------------------------------

def elements_after_heading(start: Tag) -> list:
    """Everything under a heading, up to the next heading of the same or higher level."""
    stop = {'h2', 'h3'} if start.name == 'h3' else {'h2', 'h3', 'h4'}
    out = []
    for sib in start.next_siblings:
        if isinstance(sib, Tag):
            if sib.name in stop:
                break
            out.append(sib)
    return out


def write_page(path: str, title: str, meta: str, description: str, body: list) -> None:
    lines = []
    if description:
        # Always quote: goals contain ': ', '#' and quotes, which break bare YAML.
        quoted = description.replace('\\', '\\\\').replace('"', '\\"')
        lines += ['---', f'description: "{quoted}"', '---', '']
    lines.append(f'# {title}')
    if meta:
        lines += ['', f'> {meta}']
    for block in body:
        lines += ['', block]
    text = re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip() + '\n'
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def convert_flow(flow: Page, soup: BeautifulSoup, anchors: dict, out_dir: str) -> int:
    section = soup.find(id=flow.page_id)
    if section is None:
        print(f'  !! section {flow.page_id} not found', file=sys.stderr)
        return 0

    h2 = section.find('h2')
    who = clean(h2.find(class_='who').get_text()) if h2.find(class_='who') else ''
    note = clean(h2.find(class_='fn').get_text()).strip('()') if h2.find(class_='fn') else ''
    goal_el = section.find(class_='goal')
    goal = clean(goal_el.get_text()).removeprefix('Goal:').strip() if goal_el else ''

    # Flow page: whatever sits above the first h3, then links to its steps.
    intro = []
    for el in section.find_all(recursive=False):
        if el.name == 'h3':
            break
        if el is h2 or el is goal_el:
            continue
        intro += render_flow_elements([el], anchors, skip_ids=set())

    if flow.children:
        intro.append('## In this flow')
        intro.append('\n'.join(f'* [{c.title}]({c.filename})' for c in flow.children))

    meta = ' · '.join(x for x in (who, note) if x)
    write_page(os.path.join(out_dir, flow.filename), flow.title, meta, goal, intro)
    written = 1

    for step in flow.children:
        if step.alias:              # cross-reference in the sidebar, page already exists
            continue
        head = section.find(id=step.anchor)
        if head is None:
            print(f'  !! anchor #{step.anchor} not found', file=sys.stderr)
            continue
        promoted = {sub.anchor for sub in step.children}
        # Some flows hang their nav entries off an <h3>, others straight off a
        # step <li>. h3 -> take everything up to the next h3; li -> just that item.
        if head.name in ('h3', 'h4'):
            body = render_flow_elements(elements_after_heading(head), anchors, promoted, as_headings=True)
        else:
            text, blocks = split_item(head, anchors)
            body = ([text] if text else []) + render_blocks(blocks, anchors)
        if step.children:
            is_edge = any(c.startswith('edge') for c in (head.get('class') or []))
            body.append('## Edge cases' if is_edge else '## In this step')
            body.append('\n'.join(f'* [{c.title}]({c.filename})' for c in step.children))
        write_page(os.path.join(out_dir, step.filename), step.title, flow.title, '', body)
        written += 1

        for sub in step.children:
            if sub.alias:
                continue
            li = section.find(id=sub.anchor)
            if li is None:
                print(f'  !! anchor #{sub.anchor} not found', file=sys.stderr)
                continue
            if li.name in ('h3', 'h4'):
                body = render_flow_elements(elements_after_heading(li), anchors, set(), as_headings=True)
            else:
                text, blocks = split_item(li, anchors)
                body = ([text] if text else []) + render_blocks(blocks, anchors)
            write_page(os.path.join(out_dir, sub.filename), sub.title,
                       f'{flow.title} → {step.title}', '', body)
            written += 1

    return written


def write_summary(groups: list, out_dir: str) -> None:
    lines = ['# Table of contents', '', '* [Fintalent OSW — Guides](README.md)']
    for title, flows in groups:
        if not flows:
            continue
        lines += ['', f'## {title}', '']
        for flow in flows:
            lines.append(f'* [{flow.title}]({flow.filename})')
            for step in flow.children:
                lines.append(f'  * [{step.title}]({step.filename})')
                for sub in step.children:
                    lines.append(f'    * [{sub.title}]({sub.filename})')
    with open(os.path.join(out_dir, 'SUMMARY.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(lines) + '\n')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('source', help='HTML guide, e.g. v4.html')
    ap.add_argument('--only', help='comma-separated flow codes, e.g. a1,a2')
    ap.add_argument('--out', default=REPO, help='output directory (default: repo root)')
    ap.add_argument('--no-summary', action='store_true', help='do not rewrite SUMMARY.md')
    args = ap.parse_args()

    path = args.source if os.path.isabs(args.source) else os.path.join(REPO, args.source)
    with open(path, encoding='utf-8') as fh:
        soup = BeautifulSoup(fh.read(), 'html.parser')

    groups = parse_nav(soup)
    anchors = build_anchor_map(groups)

    if args.only:
        wanted = {c.strip().lower() for c in args.only.split(',')}
        groups = [(t, [f for f in flows if f.page_id.removeprefix('page-').lower() in wanted])
                  for t, flows in groups]

    total = 0
    for title, flows in groups:
        if not flows:
            continue
        print(f'\n## {title}')
        for flow in flows:
            n = convert_flow(flow, soup, anchors, args.out)
            total += n
            print(f'  {flow.filename:<46} {n} page(s)')

    if not args.no_summary:
        write_summary(groups, args.out)
        print('\nSUMMARY.md rewritten')
    print(f'{total} page(s) written to {args.out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
