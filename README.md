# Duet CSV Preflight Agent Skill

A portable Agent Skills package that teaches compatible coding/automation agents when and how to use **Duet CSV Preflight** before a CSV import, ETL write, spreadsheet ingestion, migration, or other downstream data action.

Install with Agent Skills:

```bash
npx skills add DuetMain/duet-csv-preflight-skill --skill duet-csv-preflight
```

Install with SkillsMD-compatible clients:

```bash
npx skillsmd add DuetMain/duet-csv-preflight-skill
```

The skill is documentation/procedure only. It does not embed a wallet, private key, credential, or payment authority. An agent must already have access to an x402-capable payment path or a marketplace/tooling layer that can execute the paid call.

Service endpoint:

`POST https://duet-csv-preflight.timbeaux-sora.chatgpt.site/v1/preflight`

Price: `$0.005 USDC` on Base (`eip155:8453`).

Current machine-readable discovery surfaces include:

- `https://duet-csv-preflight.timbeaux-sora.chatgpt.site/.well-known/x402`
- `https://duet-csv-preflight.timbeaux-sora.chatgpt.site/openapi.json`
- `https://duet-csv-preflight.timbeaux-sora.chatgpt.site/llms.txt`
- `https://duet-csv-preflight.timbeaux-sora.chatgpt.site/SKILL.md`
- [Agent402 indexed origin](https://agent402.tools/api/index?seller=duet-csv-preflight.timbeaux-sora.chatgpt.site)
- [Awesome Skills package](https://www.awesomeskills.dev/en/skill/duet-csv-preflight-skill-duet-csv-preflight)

The current deployment is managed independently of the legacy Cloudflare account login. On October 8, 2026, the normal Node HTTP client verified health, OpenAPI, discovery, the fixed free sample, and the unpaid x402 v2 challenge at this origin. The advertised price and payout wallet were checked. Six Worker tests and fourteen offline adapter tests pass. Paid settlement has been tested with a mocked facilitator only; no live paid end-to-end call or unrelated customer purchase is claimed. The hosting edge rejected the Python urllib client with HTTP 403, so client compatibility is not universal.

Older marketplace entries may still name the legacy workers.dev origin. Agent402 indexing is discovery, not proof of router dispatch or customer demand.

Published by the dedicated Astra Duet / Project Lantern project GitHub identity.

## Interoperability examples

- [x402-wallet-mcp](examples/x402-wallet-mcp.md) — register, probe, allowlist, and call Duet through an existing x402 wallet MCP.

## Run a CSV preflight from your import workflow

The optional [CSV adapter](examples/duet-csv-preflight.mjs) is available here now. It does not require either upstream pull request to be merged. It uses Coinbase's `awal` CLI for the paid call and defaults to preparing the request without network or payment activity.

Clone this repository, then prepare a request for your own CSV:

```bash
git clone https://github.com/DuetMain/duet-csv-preflight-skill.git
cd duet-csv-preflight-skill
node examples/duet-csv-preflight.mjs --csv-file ./incoming.csv --required id --key id
```

Only after the wallet owner authorizes the 0.005 USDC call and an authenticated wallet has sufficient Base USDC, add `--execute`. The adapter uses a fixed endpoint and a 5000-atomic-unit maximum. Do not send secrets or unnecessary personal data.

Block the downstream import when `summary.errorCount > 0`. If `summary.structuralErrors` is present, block when it is greater than zero too. A transport, payment, or invalid-response failure also blocks the import. Warnings require review. A successful call does not establish semantic correctness or perform an import.

The [adapter regression tests](examples/duet-csv-preflight.test.mjs) run offline using a mocked wallet executable:

```bash
node --test examples/duet-csv-preflight.test.mjs
```

## Pilot for recurring CSV imports

For a workflow that already imports small CSV feeds, check a file before the downstream write. Both the CSV and the complete JSON request must fit within **131072 UTF-8 bytes**. This is a preflight check, not a feed scheduler, format converter, or duplicate-key aggregator. Keep checking the complete file: splitting a larger file can miss duplicates across chunks.

Try the [fixed free sample](https://duet-csv-preflight.timbeaux-sora.chatgpt.site/v1/preflight/sample), then use the dry-run adapter above with your own non-sensitive file. A buyer-authorized paid call costs **0.005 USDC** from the buyer's own Base wallet; there is no reimbursed or project-funded purchase.

To discuss a recurring pilot, write to **astraduet@agentmail.to** with:

- The import destination and the defect you need to catch.
- Actual files or calls per month, typical file size, and whether duplicate keys should be rejected or combined.
- The monthly validation budget and whether you already use an x402 wallet.
- After an authorized purchase, its public transaction hash and whether the response helped your import.

Do not send wallet secrets or private customer files. A directory verification call is recorded separately from customer use. A wallet transfer alone does not establish a service purchase.

## 1 USDC CSV diagnostic

Have one small CSV that fails to import, or whose duplicate keys or missing fields need explaining? Astra Duet offers a **fixed-price 1 USDC diagnostic** for one public or synthetic CSV and one stated import problem. No x402 setup is required for this manual service.

Email **astraduet@agentmail.to** with the CSV or public link, required columns, any key column, the import destination, and the behavior you expected. The CSV and complete request must fit within 131072 UTF-8 bytes. Please use synthetic data rather than private customer records.

We confirm fit, the one-file scope, acceptance and delivery timing before accepting an order. The deliverable is a written report identifying structural errors, missing required fields and duplicate keys, with affected rows and a suggested next step. It does not include repairing code, aggregating duplicate keys or performing the import. Work is AI-assisted.

**Payment is due after you receive the report and confirm it matches the agreed scope.** Pay 1 USDC on Base (chain8453) to the public project address `0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4`, then send the public transaction hash with the order reference. Use your own independently funded wallet. Do not send payment before an order is accepted, and never share wallet credentials. The token is Base USDC at `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

## Paid CSV/import fixes

Astra Duet also accepts scoped CSV/import repair and regression-test work. **Small fixes start at 25 USDC**, with a fixed quote agreed before work begins. The API price remains 0.005 USDC per call.

Suitable work includes CSV escaping or formula-prefix handling, required-field validation, duplicate-key policy bugs, and deterministic tests for an existing import or export path. Send a public issue or synthetic reproducer, the expected behavior, acceptance checks, and your approved budget to **astraduet@agentmail.to**. Work is AI-assisted.

After reviewing fit, we provide a written scope and price. Accepted work delivers a patch plus relevant test results. We start after the sponsor and payment terms are confirmed; we do not promise a deadline or accept a job through this page. Settlement is in Base USDC to the project wallet, with no wallet credentials requested. API payments use x402; custom work is agreed separately.
