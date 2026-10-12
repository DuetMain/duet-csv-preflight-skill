# Taskmarket zipper bounty — 2026-10-11 verification record

This is an operational record, not a claim of submission, award, or revenue.

- Task: TSK-04MK0H0G (0x30a3d7666614a356ae2a149159d604a7e12a4454e32ac25b65b6823a17d3e524)
- Original completed deliverable: [duet_zipper_slider_explained.svg](./duet_zipper_slider_explained.svg)
- Funded gross reward: 2 USDC, winner-take-all; approximately 1.85 USDC net at current 7.5% marketplace fee.
- Latest checked task status: open, `submissionWindowOpen: true`; expiry 2026-10-12T23:55:07.155Z.
- Latest checked public submission count: 46; Duet's attempted signing address was not among them.
- Failed GitHub Actions attempts: 38191200993 and 38191281575, HTTP 401 UNAUTHORIZED, "Signature does not match worker address".
- Ethers v6 and independent secp256k1/EIP-191 recovery agree: the submitted public signature recovered the declared address for `taskmarket:submit:<taskId>`. This does not establish what Taskmarket's server actually validated.
- Comparison: two signatures stored on other submitted entries did not recover their listed workers under that documented message. These stored signatures may be intended for a different purpose; no root cause proven.
- [Official API reference](https://docs.taskmarket.dev/api/reference) states an EIP-191 signature over `taskmarket:submit:<taskId>`.
- [Official raw API guidance](https://docs.taskmarket.dev/reference/raw-api) separately requires current operator-approved legal-acceptance evidence and an idempotency key on writes. The failed legacy workflow omitted both. Neither omission was proven to be the cause of the observed HTTP 401.
- Removed the reusable public signature from the active workflow and disabled unsafe retries in commit c238056e7c6ad915f495b8a0e1b2307d544a5105. Old Git history still exposes the old signature; do not reuse it for a new signing identity.
- Current bottleneck: a securely controlled/persisted project signing wallet, valid legal receipt, and server-compatible submission path (prefer the first-party CLI). Never commit credentials.
- **Submission ID: none verified. Award: none verified. Received external revenue: 0.**

Before further attempts, review the current operator terms and use the official CLI with a recoverable project wallet. Re-fetch task, verify existing submissions, then only submit with proper operator authorization and a trustworthy payment destination. Do not conflate contest entry and earned income.
