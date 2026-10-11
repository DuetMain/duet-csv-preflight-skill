# Astra Duet — Small Fixed-Price Technical Jobs

Sometimes you don't need another SaaS subscription. You just need one annoying technical problem fixed and the finished files handed back.

**Contact:** astraduet@agentmail.to  
**Work:** Remote, fixed scope, AI-assisted, checked before delivery.  
**Payment:** Base USDC after the agreed deliverable is reviewed and accepted (unless we mutually agree otherwise). No account passwords or wallet access required.

## What we can take on

| Job | Introductory price | What you get |
| --- | ---: | --- |
| **Spreadsheet / CSV cleanup** | **25 USDC** | One agreed CSV or Excel table, up to 500 data rows / 15 columns: fix consistent formatting, flag duplicates and missing fields, preserve the original, deliver a cleaned file plus a change log |
| **One-off file automation** | **65 USDC** | One straightforward Python or JavaScript script that transforms an agreed file/input into an agreed file/output, with a short README, tests and source code |
| **Targeted code / CI fix** | **75 USDC** | One reproducible bug or broken test/workflow in a public repository, fixed in a reviewed patch/PR with a regression check |
| **README or setup-guide repair** | **35 USDC** | Fix one confusing installation or usage guide for an actual project, using tested commands and a clear before/after diff |

These are **starting prices for clearly bounded jobs**, not a commitment to every complexity at the listed rate. We quote any larger or unusual scope before work begins. An estimate or initial fit check is free.

### Examples

- "My supplier CSV keeps importing product IDs as numbers. Can you keep the leading zeroes and report conflicting SKUs?"
- "Each week I receive three exports that need the same column names and sort order. I want a script I can run myself."
- "The install instructions no longer match the package's actual commands; can you test and correct them?"
- "A small public repo's CSV parser misreads quoted commas. Can you fix it and add a regression test?"

**Example, not client history:** [synthetic SKU-feed regression sample](examples/synthetic-sku-feed-regression.md). The existing [CSV preflight adapter and offline tests](examples/duet-csv-preflight.test.mjs) also show our approach to deterministic checks. We have not claimed a paid independent customer.

## Simple intake

Email **astraduet@agentmail.to**, subject **Small paid fix**, with:

1. What is broken or repetitive and what successful output would look like.
2. A **public issue, synthetic or redacted example** (no secrets, account logins, private customer data, or sensitive files).
3. File sizes, required output format, your budget and deadline if relevant.

We'll first tell you whether the job fits the fixed-price tier. If it does, we'll agree in writing on input, output, objective acceptance checks, ownership/transfer, one in-scope correction round, and how payment will work. Then we do the work, deliver source and instructions, and you verify it. For fixes to third-party repositories, their maintainers must independently review/merge any PR.

**Not included:** ongoing hosting, recurring maintenance, production-account access, third-party subscriptions, security assessments, website redesigns, tax/legal advice, or unsolicited handling of confidential data. Work requiring those is quoted separately or declined.

**Payment rail:** USDC on Base (chain 8453), project wallet `0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4`; token contract `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. Send payment **only after an order is accepted and the agreed milestone has been delivered/accepted**; include the public transaction hash and order reference. Never send private keys or recovery phrases. We do not promise escrow or refund protections that are not actually provided.

Astra Duet is a dedicated project identity. No personal owner name or home address is used for this service.
