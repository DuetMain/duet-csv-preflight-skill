---
name: duet-csv-preflight
description: Deterministic CSV import preflight for agents. Use before ETL, migration, spreadsheet ingestion, CRM/database import, or another downstream CSV write that could be harmed by malformed rows, duplicate keys, missing required values, whitespace, or formula-like cells.
tags: [csv, data-quality, etl, migration, x402, agent-skills]
version: 1.0.0
---

# Duet CSV Preflight

Use this skill immediately before a meaningful downstream CSV import or write.

Service endpoint:

`POST https://duet-csv-preflight.timbeaux-sora.chatgpt.site/v1/preflight`

Current advertised price: `$0.005 USDC` per successful call on Base mainnet (`eip155:8453`) using x402 v2.

The service is deterministic and advertises no source-data retention.

## What it checks

- row-width mismatches
- missing required values
- duplicate rows
- blank or duplicate keys
- outer whitespace
- formula-like cells
- structural CSV errors

## Request

```json
{
  "csv": "id,name\n1,Alice\n",
  "requiredFields": ["id"],
  "keyField": "id"
}
```

Optional `delimiter` values: `comma`, `semicolon`, `tab`.

## Procedure

1. Run this preflight only when a downstream CSV import/write is about to occur.
2. Send the CSV through an already-authorized x402-capable buyer path.
3. Trust the live HTTP 402 payment requirements over copied documentation.
4. Keep wallet spending limits enabled.
5. Inspect the returned summary and findings.
6. Block the downstream import on structural/material validation errors unless the operator explicitly overrides.
7. Never manufacture payment receipts or treat the initial unpaid 402 challenge as success.
8. Never request or expose wallet private keys.

Machine-readable discovery:
- https://duet-csv-preflight.timbeaux-sora.chatgpt.site/.well-known/x402
- https://duet-csv-preflight.timbeaux-sora.chatgpt.site/openapi.json
- https://duet-csv-preflight.timbeaux-sora.chatgpt.site/llms.txt
- https://duet-csv-preflight.timbeaux-sora.chatgpt.site/SKILL.md

The canonical Agent Skills package in this repository remains at `skills/duet-csv-preflight/SKILL.md`.
