# Astra Duet — independently verified revenue sprint ledger
Date checked: 2026-10-11 late evening America/Chicago (2026-10-12 UTC)
Owner identity for GitHub actions: DuetMain
Purpose: cash-first accounting, not an activity score. No personal identifying information, credentials or private keys.

## Money reconciliation

| Bucket | Verified amount | Evidence/qualification |
| --- | ---: | --- |
| Independently funded organic customer revenue | 0 USD / 0 USDC | No externally identified customer sale, paid bounty award, or independently attributable escrow settlement |
| Settled independent bounty awards | 0 | No accepted/payout entry for Duet |
| Project-funded test / internal receipts | Separately tracked, not organic | Current Base public wallet has four inbound USDC transfers of 0.005 USDC each, all dated on or before 2026-10-08; source of each transfer not independently established as a customer |
| Trading and gambling realized gains | Excluded | Separate user-controlled financial activity, not Duet organic service income; no account trade performed by this sprint |
| New third-party spending | 0 | No paid platform calls, gas funding, wallet signup, purchases or metered browser runs |
| Signed customer orders | 0 confirmed | Contact attempts are not orders |

Public receiving address (Base): `0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4`
Read-only token transfer evidence: https://base.blockscout.com/api/v2/addresses/0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4/token-transfers?type=ERC-20

## Executed and independently checked

1. Verified current `bounties/taskmarket-zipper-2026/SUBMISSION_STATUS.md` and disabled legacy `.github/workflows/taskmarket-zipper-submit.yml`; no public reusable signing secret remains in current workflow (old Git history remains public).
2. Corroborated live funded Taskmarket zipper task `TSK-04MK0H0G` still open with **46** submissions; no Duet worker entry, no submission ID, no award. Existing EIP-191 plain-message signature locally recovered its declared wallet address but backend returned HTTP 401.
3. Independently found reported Taskmarket browser/CLI contract mismatch in https://github.com/daydreamsai/skills-market/issues/66: the published CLI 1.13.0 uses an artifact-key-bound signature for its final `submissions/from-keys` request, unlike the browser's plain-message reuse. Raw API endpoint `submissions.submit` may differ; root cause remains **unconfirmed**. Posted new DuetMain corroboration https://github.com/daydreamsai/skills-market/issues/66#issuecomment-6117336044, without exposing any signing material.
4. Project Lantern Gmail, `astraduet@agentmail.to` and `webfix@agentmail.to` checked: no incoming accepted, independently funded job or payment notice observed. Outbound outreach and delivery-failure notices excluded from revenue.
5. Live ArcBounty API https://arcbounty.app/api/v1/stats showed **22.77 USDC paid** to workers, 12 completed jobs of which 7 completed by agents. Strong evidence its payout rail *has* settled on Arc mainnet, not evidence of independent customers or that Duet can earn there. Live https://arcbounty.app/api/v1/bounties?status=open returned **0** open jobs (2026-10-12T03:43:49Z). Network writes require an Arc signing wallet and native-USDC gas; none authorized/funded by this run.
6. Rejected stale advertised bounties after checking authoritative GitHub issue state: Sottara-Labs/sottara#101 ($60) closed, Specula-Labs/specula-app#9 ($60) closed, tscircuit/jlcsearch#92 ($75) closed, and tscircuit/tscircuit#1130 closed. Visible listings alone do not prove a spendable budget or open work.
7. Bountyboard-demo#17 open but amount/escrow/independent payment not substantiated. BasedHardware/omi proposed bounties have not been approved as funded; duplicate reports are not paid new work.

## Lessons from confirmed external payouts

- `https://arcbounty.app/developers` and `https://arcbounty.app/api/v1/stats` document mainnet onchain escrow, concrete acceptance/review controls, and actual paid transactions. But 0 open work means **do not claim there is a Duet opportunity today**.
- `https://shaduf.ai/p/agentic-freelance/opportunities/` separately analyzes marketplace rails; payout reliability and outside buyer identity are distinct from headline task volume. Compare those before beginning any unpaid/speculative work.
- `https://algora.io/pricing/` documents outcomes-based payout; nonetheless numerous stale/closed GitHub issues remain in marketplace catalogs, and Stripe/payee onboarding may be required.
- Earning pattern: independently funded scope -> verify exclusive/low-contest availability and acceptance rules -> claim legitimately -> deliver with direct evidence -> receive approval -> confirm settled *independent* payment. A merged PR or accepted task without disbursement is not cash.
- Duet should favor **requester-confirmed, exclusive small IT/CSV repair orders** through existing fixed-price services over unsolicited mass outreach and winner-take-all microcontests, while continuing to test verified funded job rails. Crypto-only receiving instructions may limit normal small-business conversion. Do not create new account, wallet, schedule, paid integration, or trade without appropriate authorization.

## Next gate

1. One genuine *funded* and currently available job, with documented scope, acceptance, independence and payout rail; or one explicit buyer-accepted order for a fixed-price service.
2. Meet exact acceptance, deliver, capture receipt/merge/review evidence.
3. Verify settled payment from an independent payer, book gross/fees/net once, and notify user.
4. Taskmarket zipper is blocked until safely controlled signing identity and server-supported auth/CLI path. Don't repeat unsafe signing attempts.

**Current outcome: independently verified organic income = $0. Work performed and platform payability research are not revenue.**
