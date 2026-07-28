#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert the OSW HTML guides into GitBook-ready markdown pages.

The HTML files are the source of truth. Re-run this after editing them:

    python tools/html-to-gitbook.py v4.html
    python tools/html-to-gitbook.py v4.html --only a1,a2     # pilot subset

One <section id="page-XX"> becomes one .md file at the repo root, so image
links stay relative to the images that already live there.
"""
import argparse
import os
import re
import sys

from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# Inline tags rendered as markdown emphasis.
EMPHASIS = {'b': '**', 'strong': '**', 'i': '*', 'em': '*', 'code': '`'}


def slugify(text: str) -> str:
    """'A1 · Create an SDR / KAM account' -> 'a1-create-an-sdr-kam-account'."""
    text = text.lower().replace('&', ' and ')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def clean(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


def inline(node, anchors: dict) -> str:
    """Render an inline subtree to markdown."""
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
            href = anchors.get(href[1:], href)  # cross-page anchors -> page.md#slug
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
    head, body = rows[0], rows[1:]
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * width]
    out += ['| ' + ' | '.join(r) + ' |' for r in body]
    return '\n'.join(out)


def render_figure(fig: Tag, anchors: dict, indent: str = '') -> str:
    img = fig.find('img')
    if not img:
        return ''
    src = img.get('src', '')
    alt = clean(img.get('alt', ''))
    out = [f'{indent}![{alt}]({src})']
    cap = fig.find('figcaption')
    if cap:
        # Captions are already italic; drop inner bold so we don't emit '***x***'.
        text = clean(inline(cap, anchors)).replace('**', '')
        if text:
            out.append(f'{indent}*{text}*')
    return '\n\n'.join(out)


def render_list_item(li: Tag, anchors: dict, number: int) -> str:
    """A step: '1. **A1.1** — text', with figures/tables indented under it."""
    blocks, text_parts = [], []
    for child in li.children:
        if isinstance(child, Tag) and child.name in ('figure', 'table', 'ol', 'ul'):
            if child.name == 'figure':
                blocks.append(render_figure(child, anchors, indent='   '))
            elif child.name == 'table':
                blocks.append('\n'.join('   ' + l for l in render_table(child, anchors).splitlines()))
            else:  # nested list -> flatten as indented bullets
                for sub in child.find_all('li', recursive=False):
                    blocks.append('   - ' + clean(inline(sub, anchors)))
        else:
            text_parts.append(inline(child, anchors))

    text = clean(''.join(text_parts))
    code = li.get('data-code')
    line = f'{number}. **{code}** — {text}' if code else f'{number}. {text}'
    return '\n\n'.join([line] + [b for b in blocks if b])


def render_section(sec: Tag, anchors: dict) -> tuple[str, str]:
    """Return (title, markdown body) for one <section id="page-XX">."""
    h2 = sec.find('h2')
    who = clean(h2.find(class_='who').get_text()) if h2.find(class_='who') else ''
    code = clean(h2.find(class_='n').get_text()).rstrip('·').strip() if h2.find(class_='n') else ''
    note = clean(h2.find(class_='fn').get_text()) if h2.find(class_='fn') else ''
    for tag in h2.find_all(class_=['who', 'n', 'fn']):
        tag.decompose()
    title = clean(h2.get_text())
    full_title = f'{code} · {title}' if code else title

    goal_el = sec.find(class_='goal')
    goal = clean(goal_el.get_text()).removeprefix('Goal:').strip() if goal_el else ''

    lines = []
    if goal:
        lines += ['---', f'description: {goal}', '---', '']
    lines.append(f'# {full_title}')
    meta = ' · '.join(x for x in (who, note.strip('()')) if x)
    if meta:
        lines += ['', f'> {meta}']

    for el in sec.find_all(recursive=False):
        if el is h2 or el is goal_el:
            continue
        classes = el.get('class') or []
        if el.name == 'nav' or any(c.startswith('pagernav') for c in classes):
            continue  # prev/next pager belongs to the HTML layout, not the page
        if el.name == 'h3':
            lines += ['', f'## {clean(el.get_text())}']
        elif el.name == 'ol':
            lines.append('')
            for i, li in enumerate(el.find_all('li', recursive=False), 1):
                lines += [render_list_item(li, anchors, i), '']
        elif el.name == 'table':
            lines += ['', render_table(el, anchors)]
        elif el.name == 'figure':
            lines += ['', render_figure(el, anchors)]
        elif el.name in ('p', 'div'):
            text = clean(inline(el, anchors))
            if text:
                lines += ['', text]

    body = '\n'.join(lines)
    return full_title, re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'


def build_anchor_map(sections: list, filenames: dict) -> dict:
    """anchor id -> 'page.md#heading-slug', so in-HTML jump links keep working.

    Only h3 headings survive as markdown anchors. An id on a step (<li id="ea-1-1">)
    resolves to the heading it sits under, which is the closest honest target.
    """
    anchors = {}
    for sec in sections:
        page = filenames[sec['id']]
        current = page
        for el in sec.find_all(['h3', 'li', 'div'], id=True):
            if el.name == 'h3':
                current = f'{page}#{slugify(clean(el.get_text()))}'
                anchors[el['id']] = current
            else:
                anchors[el['id']] = current
    return anchors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('source', help='HTML guide, e.g. v4.html')
    ap.add_argument('--only', help='comma-separated page codes, e.g. a1,a2')
    ap.add_argument('--out', default=REPO, help='output directory (default: repo root)')
    args = ap.parse_args()

    path = args.source if os.path.isabs(args.source) else os.path.join(REPO, args.source)
    with open(path, encoding='utf-8') as fh:
        soup = BeautifulSoup(fh.read(), 'html.parser')

    sections = [s for s in soup.find_all('section') if (s.get('id') or '').startswith('page-')]
    if not sections:
        print(f'no <section id="page-..."> found in {args.source}', file=sys.stderr)
        return 1

    wanted = {c.strip().lower() for c in args.only.split(',')} if args.only else None

    # First pass: filenames for every page, so cross-page anchors resolve.
    filenames = {}
    for sec in sections:
        h2 = sec.find('h2')
        code = clean(h2.find(class_='n').get_text()).rstrip('·').strip() if h2.find(class_='n') else ''
        for tag in h2.find_all(class_=['who', 'n', 'fn']):
            tag.extract()  # extract, not decompose — render_section needs a clean copy later
        filenames[sec['id']] = slugify(f'{code} {clean(h2.get_text())}') + '.md'

    # Re-parse: the first pass mutated the tree while collecting filenames.
    with open(path, encoding='utf-8') as fh:
        soup = BeautifulSoup(fh.read(), 'html.parser')
    sections = [s for s in soup.find_all('section') if (s.get('id') or '').startswith('page-')]

    anchors = build_anchor_map(sections, filenames)

    written = []
    for sec in sections:
        page_code = sec['id'].removeprefix('page-').lower()
        if wanted and page_code not in wanted:
            continue
        title, body = render_section(sec, anchors)
        name = filenames[sec['id']]
        with open(os.path.join(args.out, name), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(body)
        written.append((page_code, title, name))
        print(f'  {name:<48} {title}')

    print(f'\n{len(written)} page(s) written to {args.out}')
    print('\nSUMMARY.md entries:')
    for _, title, name in written:
        print(f'  * [{title}]({name})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
