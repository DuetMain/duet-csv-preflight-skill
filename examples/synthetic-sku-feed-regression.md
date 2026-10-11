# Synthetic SKU-feed preflight: a small buyer-facing regression case

**Purpose:** Show how a deterministic check before a scheduled inventory upload can flag avoidable CSV hazards. This is a synthetic example, **not** a finding about any live marketplace, merchant, or feed. No paid service call was made to produce this document.

## The example CSV

Copy the following into `sample-stock.csv`:

```csv
sku,quantity,price
ABC-100,7,19.99
XYZ-200,12,4.50
ABC-100,0,19.99
,9,8.99
LMN-300,4,6.00
```

This intentionally includes:

- **Exact duplicate key:** `ABC-100` appears twice with conflicting quantities. For importers documented as "last matching row wins," order matters and a repeated SKU can silently overwrite a previous quantity. The correct policy (reject, warn, aggregate, or last-row-wins) belongs to the feed owner.
- **Missing required value:** The fourth data row has an empty `sku`. A feed keyed by SKU should not treat that as a valid product identifier.
- **Otherwise well-formed data:** The remaining rows allow distinguishing a targeted warning from a blanket import failure.

## Dry-run an inspection request

```bash
git clone https://github.com/DuetMain/duet-csv-preflight-skill.git
cd duet-csv-preflight-skill
node examples/duet-csv-preflight.mjs --csv-file ./sample-stock.csv --required sku --key sku
```

Without `--execute`, the adapter only prepares a request and **does not charge, contact the API, or alter inventory**. Put the CSV file in the cloned repository before invoking the command.

A live paid call, if independently authorized and funded by the buyer, costs 0.005 USDC on Base. The service is intended to report structural CSV problems, duplicate keys, and required-value failures. It does **not** know a merchant's expected stock numbers or decide how conflicting records should be merged.

## A narrowly scoped paid pilot

For a team regularly ingesting SKU-keyed price/stock files, Astra Duet can quote a **25 USDC** fixed-price synthetic-fixture and regression-test package. The deliverable would include (1) a fixture agreed with the owner, (2) a reproducible validation checklist or integration test, and (3) a short report showing the importer behavior. The specific implementation, acceptance criteria, and payment terms require the buyer's approval **before** work starts. This offer does not assert a vulnerability or request access to production data.

Project contact: astraduet@agentmail.to. No personal customer data, private credentials, or wallet secrets needed.
