# B3.3 · Create Client Invoice

> B3 · Timesheet → invoice (Admin)

1. **B3.3.1** — Click **Create Client Invoice** (on the talent's row in Timesheets, or via **Client Invoices → Create new Client Invoice**).

   ![Create Client Invoice button](sdrx-ts-07-admin-row.png)

   *B3.3.1 — ④ Create Client Invoice, right on the talent's row.*

2. **B3.3.2** — **The form prefills from the contract** — check every field: The **“X hrs to bill · Y hrs worked”** warning is repeated right above **Quantity** — read it one last time here.

   | Field | Must be |
   |---|---|
   | **Contract / Project / Client** | the contract you are actually billing. |
   | **Service period start / end** | the uninvoiced date range ([B3.1.4 ↗](b3-1-view-and-sync-data.md)). |
   | **Issued Date** | defaults to today. |
   | **Billing rate** | = the **billing rate** on the contract (what the client pays). |
   | **Quantity** | **= hours to bill** (Hourly) or **= days to bill** (Daily) — **not** the logged hours. |
   | **Amount** | calculated as Quantity × Billing rate. **Multiply it yourself as a check.** |
   | **Currency · Fintalent Bank** | as per the contract (e.g. EUR → WISE EUR). |
   | **Client billing address · VAT** | as per the contract. |
   | **Description** | talent name + period. |

   ![Create Client Invoice form](sdrx-ts-09-admin-invoice-form.png)

   *B3.3.2 — Service period · Billing rate · Quantity = hours to bill · Amount calculated.*

3. **B3.3.3** — **Review the expense reports (if the talent filed any).** Expenses do **not** sit on the fee line — they land at the bottom of the form, one row each. Check each of them: To drop an invalid item from this invoice, click **⊖** at the start of its row; to add something beyond the fee, click **⊕ Additional items**. An expense the talent filed is missing?It falls outside the **Service period** — usually because the talent dated it on a day with no billable hours. Widen the date range and it appears: see [B2.x.8 ↗](b2-x-8-expense-on-a-non-worked-day.md).

   | What to look at | Check against |
   |---|---|
   | **Description** | What the talent wrote — clear enough that the client understands what they are paying for. |
   | **Currency** | Matches the contract currency. |
   | **Quantity × Amount = Total** | Calculated; **Total EUR** is what actually joins the invoice. |
   | **File invoice expense** | The receipt. *“no files yet”* means **the talent attached nothing** — ask for it before billing, or **Upload File** yourself if you received it another way. |

   ![Expense block inside the invoice form](tsx-18-admin-check-expense.png)

   *B3.3.3 — ① Description · Currency · Quantity · Amount · ② Total EUR joining the invoice · ③ the receipt attachment (currently \*no files yet\*) · ④ drop this item · ⑤ add a new one.*

4. **B3.3.4** — When everything checks out, click **Create**. The invoice is created in **Draft**, tagged **Timesheets (date range)** — review it straight away in [B3.4 ↗](b3-4-review-invoice-and-pdf.md). If there were expenses, the total already includes them.
