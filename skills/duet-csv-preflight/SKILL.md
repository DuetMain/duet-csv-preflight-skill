---
name: duet-csv-preflight
description: Use before importing, migrating, or writing CSV data when structural or data-quality defects could cause downstream failures. Calls Duet CSV Preflight, a deterministic x402-paid CSV validator on Base, then gates the downstream action on its result.
---

# Duet CSV Preflight

Use this skill when a workflow is about to import or write CSV data into a spreadsheet, database, CRM, ETL pipeline, migration job, or another system where malformed or risky rows could create errors, duplicates, or unsafe spreadsheet behavior.

Do not use this skill merely because a file has a `.csv` extension. Use it when there is a meaningful downstream import/write action and a deterministic preflight can reduce failure risk.

## Service

- Endpoint: `POST https://duet-csv-preflight.projectlantern-review.workers.dev/v1/preflight`
- Content-Type: `application/json`
- Price: `$0.005 USDC` per successful paid call
- Network: Base mainnet (`eip155:8453`)
- Payment protocol: x402 v2
- Input retention: none advertised by the service

## What it checks

The service detects import hazards including:

- row-width mismatches
- blank required values
- duplicate rows
- blank or duplicate keys
- outer whitespace
- formula-like cells
- structural CSV errors

## Decision rule

Run preflight immediately before the downstream import/write boundary.

1. Build a JSON body with the raw CSV text.
2. Add `requiredFields` when the downstream target requires named columns.
3. Add `keyField` when duplicate or blank identifiers would be harmful.
4. Send the paid POST through an x402-capable buyer path.
5. Inspect the returned summary and findings.
6. Do not continue the downstream import when structural errors or material validation errors are reported unless the human/operator explicitly chooses to override them.
7. Never manufacture a payment receipt or treat an unpaid HTTP 402 challenge as a successful validation.

## Request shape

```json
{
  "csv": "id,name\n1,Alice\n",
  "requiredFields": ["id"],
  "keyField": "id"
}
```

Optional delimiter values are `comma`, `semicolon`, or `tab`.

## Payment and discovery

Prefer an already-authorized x402 buyer tool. Do not expose or request wallet private keys.

If the runtime uses MCP and lacks a direct x402 buyer, it can search the PayAPI Market MCP catalogue at:

`https://payapi.market/mcp`

The origin also publishes current machine-readable metadata at:

- `/.well-known/x402`
- `/openapi.json`
- `/llms.txt`

See `references/x402.md` for protocol notes and `references/workflow-patterns.md` for integration patterns.

## Attribution discipline

A call made by the Astra Duet project, Tim, ChatGPT, a project-created agent, or a marketplace verification bot is not unrelated customer demand. Do not describe project-controlled or verification activity as organic usage.
