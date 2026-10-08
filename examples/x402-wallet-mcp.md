# Using Duet CSV Preflight with x402-wallet-mcp

This is a third-party interoperability example. Duet CSV Preflight is not maintained or endorsed by x402-wallet-mcp.

Duet publishes a standard `/.well-known/x402` discovery document and can be registered with x402-wallet-mcp using its existing tools.

## 1. Add the discovery source

Ask the agent to call `add_endpoint_source` with:

```json
{
  "base_url": "https://duet-csv-preflight.timbeaux-sora.chatgpt.site"
}
```

## 2. Probe before paying

Use `query_endpoint` against:

```
https://duet-csv-preflight.timbeaux-sora.chatgpt.site/v1/preflight
```

Trust the live HTTP 402 payment requirements over copied documentation.

## 3. Allow the advertised payee if your wallet allowlist is enabled

Current documented payout address:

```
0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4
```

Before adding any merchant, confirm the live 402 challenge advertises the expected payee, network, asset, and amount. Keep wallet spending limits enabled.

## 4. Call the endpoint

Example `call_endpoint` input:

```json
{
  "url": "https://duet-csv-preflight.timbeaux-sora.chatgpt.site/v1/preflight",
  "method": "POST",
  "body": "{\"csv\":\"id,name\\n1,Alice\\n\",\"requiredFields\":[\"id\"],\"keyField\":\"id\"}"
}
```

Current documented price is $0.005 USDC on Base mainnet (`eip155:8453`) per successful call.

## Safety

- Do not expose or request private keys.
- Keep per-call and daily spending limits enabled.
- Do not treat an unpaid HTTP 402 challenge as a successful preflight.
- Do not assume a passing structural preflight means the data is semantically correct.
- Re-read the live payment requirements before every paid call.
