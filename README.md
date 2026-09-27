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

Published by the dedicated Astra Duet / Project Lantern project GitHub identity.
