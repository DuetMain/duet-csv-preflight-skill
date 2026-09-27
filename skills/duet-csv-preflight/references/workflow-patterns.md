# Workflow patterns

## CSV import / ETL gate

1. Obtain raw CSV text.
2. Run Duet CSV Preflight.
3. If structural errors or material findings exist, stop and surface them.
4. If acceptable, continue to the import/write node.

Useful before:

- CSV-to-database imports
- CRM contact imports
- spreadsheet uploads
- data migration scripts
- n8n / automation-platform file ingestion
- MCP tools that submit CSV/XLSX-derived records

## CSVbox REST File API

CSVbox's public REST File API documentation states that files submitted through that API are pushed to the configured destination in raw form and are not validated using the sheet's configured rules. That makes a deterministic external preflight particularly relevant immediately before an automated `submit_file` call.

Potential chain:

`agent obtains CSV -> Duet preflight -> if acceptable -> CSVbox submit_file`

This skill does not modify CSVbox and does not imply CSVbox endorses Duet.
