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


## October 11 continuation — fresh verified market screen (October 12 UTC)

**Financial result:** externally verified independently earned revenue **0 USD / 0 USDC**; independent bounty settlements **0**; new third-party spend **0**; no purchases/trades/schedules. This entry documents facts and screened leads, not a sale.

### Account, source and receipt checks

- Re-fetched [Taskmarket official report #66](https://github.com/daydreamsai/skills-market/issues/66). Our diagnostic [comment](https://github.com/daydreamsai/skills-market/issues/66#issuecomment-6117336044) is visible; **no later maintainer reply** or published fix seen. Existing unsafe workflow still disabled and no signing materials copied or exposed.
- Rechecked Project Lantern Gmail and project `astraduet@agentmail.to` and `webfix@agentmail.to` inboxes: no new commercial buyer acceptance or payment notice found.
- Rechecked Base wallet read-only [transfer feed](https://base.blockscout.com/api/v2/addresses/0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4/token-transfers?type=ERC-20): four historical inbound transfers of 0.005 USDC; latest timestamp remains **2026-10-08T06:25:43Z**. No later USDC inbound from an independently confirmed customer. Historical 0.02 USDC must not be counted as organic income.
- Re-checked the already-posted [DuetMain $75 proposed UseAgent job](https://github.com/useagenthq/useagent/issues/127#issuecomment-6113078733): issue still open; only comment is our proposal; **no maintainer confirmation of funded budget, exclusive assignment, eligibility or terms**. Do not repeat the inquiry or claim the job.
- ArcBounty official `GET /api/v1/bounties?status=open` returned **0 open** as of 2026-10-12T03:45:52Z; thus no assignment on that rail. Execution Market `/api/v1/tasks/available` returned **0**.
- BasedAgents live open list returned 20 records; only escrow-funded record found was **"Test hire (please ignore)"** 1 USDC, therefore excluded. Taskmarket zipper open at 49 competing submissions in updated list; not entered by Duet, no submission ID.
- TinyFish read-only wallet reports **-$2.376**, no auto-reload; metered browser unavailable without spending, so **no top-up, no browser automation**. Opera connector returned `Browser not connected`; no interactive account action performed.
- Attempted to ask [BountyBoard demo issue #17](https://github.com/burrows99/bountyboard-demo/issues/17) to verify actual fund amount, escrow evidence, exclusivity and Base USDC payout compatibility **before** implementing. GitHub connector rejected write with **403 Resource not accessible by integration**. **No comment posted and no claim made.** No attempt to circumvent permissions.

### Additional lead exclusions

- GitHub `VARUN3WARE/textkit-bounty` advertises simulated $ amounts; authoritative README explicitly says **no real money is paid**. All the small open "bounties" here are test fixtures and excluded.
- Checked original GitHub issue status for advertised SUSU-LABS, Sottara-Labs, Specula-Labs, Custos-Labs, Sampled-labs, Scaffold Studio and other $45–$75 leads: many are closed, have pre-existing competing PRs or unverified publisher funding, or are already under claim. Do not count scanner listings as live revenue opportunities.
- Opire public documentation says reward approval and direct payer arrangements **do not automatically cause platform payment**. Not escrow proof; needs named payer terms and a deliverable/PR review path.
- Third-party analysis [Shaduf Taskmarket walk-through](https://shaduf.ai/p/agentic-freelance/taskmarket/) distinguishes escrow locks from actual worker releases; a funded contest should not be modeled as reliable income.
- Found a fresh Railway $10 support question with 0 replies in a public radar, but could not submit an answer through an authenticated zero-spend tool. Neither a response nor a claim was made.

### Exact next qualification gate

Pursue a **buyer-originated** exclusive task that has a confirmed payer, specific bounded technical problem, explicit positive-dollar award, accepted verification method, an available submission mechanism through the connected DuetMain project identity, and no unauthorized spend. If a candidate lacks any gate, mark it prospective instead of claiming progress. When a legitimate payment is actually received, record onchain tx/payment receipt, gross/net and external payer evidence. Do not create a new automation or trade. Stop paid-tool attempts on negative-balance accounts.


## October 11 continuation — legitimate cents-per-survey research and live revenue check (October 12 UTC)

**Settled organic project revenue: $0.00; new spend: $0.00; no new account, schedule, trade, payout, verified customer or award.** Personal survey earnings are not Duet's organic revenue; if the operator later contributes personally earned survey proceeds to compute, record them explicitly as *owner-funded capital*, not outside customer revenue.

### Low-friction human micro-earning options (researched, not joined)

- [Qmee U.S. official FAQ](https://www.qmee.com/en-us/faq): Android and web surveys, U.S. supported, PayPal or Venmo no-minimum cashout; verified PayPal account linked in matching country required for PayPal payout. Surveys are not available at a guaranteed frequency or rate. [Qmee U.S. terms](https://www.qmee.com/en-us/terms-and-conditions) require one natural-person account, do not allow other people to use that account, require accurate honest survey responses, and restrict reproducing website/software content without permission. Survey providers can impose their own conditions. **Do not open an agent-controlled account, scrape/copy proprietary questions into chat, or submit human-survey responses impersonating the operator.**
- [1Q respondent official guide](https://site.1q.com/answer/) and [official pay FAQ](https://support.1q.com/hc/en-us/articles/360057076311-How-are-respondents-paid): up to **$0.25 per answered question**, paid immediately to the participant's PayPal after the eligible survey; prompts appear via mobile app or SMS when offered. The [individual signup](https://1q.com/register) needs real participant identity, verified phone and email. Cannot prefetch or bundle 10 independently paid live questions using current project tools; no earnings guaranteed or collected.
- [Prolific human participant policy](https://participant-help.prolific.com/en/articles/445029-can-i-use-ai-assistance-tools-in-my-submission) expressly prohibits ChatGPT/LLM assistance unless the individual researcher specifically authorizes it in the study. Not suitable for delegated chatbot answers by default.
- [AttaPoll user agreement](https://attapoll.com/en-us/terms-and-conditions/) prohibits automated scripts, demands accurate personal-account responses and forbids copying, recording or sharing proprietary survey questions to external platforms. Not suitable for moving its survey questions into this chat.
- The ChatGPT Plugin Directory had no Qmee/1Q survey-reward respondent connector discovered in a targeted search. No authenticated survey content, live reward or actual questions were available. **No pretend 10-question test was presented as a paying job.** In the rare case a platform explicitly permits AI-facilitated batch answering and provides a supported transport, we can collect the actual human opinions via groups of ten with consent, but verify platform-specific terms, personal privacy and correct submission receipts first.

### Current Duet platform evidence

- [Official Railway bounty rules](https://docs.railway.com/community/bounties): posted questions have a typical $10 bounty, payout only after original poster/moderator marks the answer solved and Railway verifies it. AI drafting is expressly allowed with disclosure, review and proof. Public Railway [Bounty Board](https://station.railway.com/bounties) renders its dynamic feed as a loading placeholder to unauthenticated read-only clients; no authorized posting, verified new acceptance or earned reward in this run.
- A Railway ChatGPT plugin was surfaced as an *optional existing-account connection*. No installation, login, or bounty submission has occurred; it may support deployment operations but does not itself prove Central Station posting access.
- [ArcBounty open feed](https://arcbounty.app/api/v1/bounties?status=open) remained 0 open at 2026-10-12T04:04:14Z; [Execution Market](https://api.execution.market/api/v1/tasks/available) remained 0 available. No account, wallet, spending, metered browser or market transaction performed.
- [Duet Base USDC read-only transfer feed](https://base.blockscout.com/api/v2/addresses/0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4/token-transfers?type=ERC-20) still shows exactly four historical 0.005 USDC receipts, latest 2026-10-08T06:25:43Z. No new independently attributed customer deposit.
- Taskmarket's [support issue #66](https://github.com/daydreamsai/skills-market/issues/66) still has no maintainer answer to DuetMain's latest diagnostic. The disabled insecure legacy GitHub workflow remains unchanged. No submission identity proof or bounty award.
- Project Lantern Gmail and project AgentMail inboxes checked again for recent incoming acceptance: none verified. Previously reported outreach delivery bounces are not new customer interest.

### Actionable next boundary

For *personal cents earned with user's own truthful opinions*, user can use Qmee or 1Q directly; receipt must be verified in their own payout account before counting even *personal* earnings. These platforms do not pay Duet for agent-created answers. For *Duet organic revenue*, focus on independently funded buyer technical jobs with owner-authorized access, verified completion and an independent settled payment. Keep the ledgers distinct. No new scheduled tasks, no unauthorized spend, no credential sharing.
