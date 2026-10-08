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

`POST https://duet-csv-preflight.projectlantern-review.workers.dev/v1/preflight`

Price: `$0.005 USDC` on Base (`eip155:8453`).

Current machine-readable discovery surfaces include:

- `https://duet-csv-preflight.projectlantern-review.workers.dev/.well-known/x402`
- `https://duet-csv-preflight.projectlantern-review.workers.dev/openapi.json`
- `https://duet-csv-preflight.projectlantern-review.workers.dev/llms.txt`
- `https://duet-csv-preflight.projectlantern-review.workers.dev/SKILL.md`
- PayAPI Market MCP: `https://payapi.market/mcp`
- x402scan: `https://www.x402scan.com/server/fb98d06a-a83e-42fa-870b-d8b5d00f7a89`
- agent-tools.cloud: `https://agent-tools.cloud/services/duet-csv-preflight-projectlantern-review-workers-dev-sub983`
- Awesome Skills: `https://www.awesomeskills.dev/en/skill/duet-csv-preflight-skill-duet-csv-preflight`
- Agent402 index: `https://agent402.tools/marketplace`

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
