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


## Continued cash-first sprint — Oct 11 local / Oct 12 UTC (commit after 6e3c6ab)

**Settled independent revenue: $0 USD / $0 USDC; new spending: $0; accepted buyer contracts: none established; new bounty awards: none; no new trades, scheduled tasks, or survey accounts.** This is a read-only opportunity investigation, not earnings.

### Reconciled project evidence

- Re-verified source record and `.github/workflows/taskmarket-zipper-submit.yml`. The unsafe Taskmarket legacy submission workflow remains disabled (blob `671cb40009fd40f1569d15297c5c4456e394a45f`); do not change or replay a signature.
- [Taskmarket support issue #66](https://github.com/daydreamsai/skills-market/issues/66): only preexisting comments and DuetMain's [diagnostic comment](https://github.com/daydreamsai/skills-market/issues/66#issuecomment-6117336044); no new maintainer reply, supported authentication fix, submission receipt, or award.
- Fresh Project Lantern Gmail and project `astraduet@agentmail.to`, `webfix@agentmail.to`, and `duetimportcheck@agentmail.to` checks show no newly verified customer order or payout. Recent mail observed contains Railway welcome notices and previously known delivery-failure bounces, not money.
- Read-only Base Blockscout [ERC-20 transfer feed](https://base.blockscout.com/api/v2/addresses/0xa9a52a066e342e2ED2488BBdb9fAd95EFd3D9FD4/token-transfers?type=ERC-20) still lists four historical 0.005 USDC receipts, latest **2026-10-08T06:25:43Z**. These 0.02 USDC historical internal/unattributed receipts are **not** independently earned customer revenue.
- Current [ArcBounty open jobs](https://arcbounty.app/api/v1/bounties?status=open) = 0; [Execution Market available jobs](https://api.execution.market/api/v1/tasks/available) = 0. BasedAgents live open listing returned 20, only escrow-funded entry title `Test hire (please ignore)`, hence expressly excluded.

### Fresh real-platform screening, no assignments

- Official [Railway bounty program](https://docs.railway.com/community/bounties) is an actual $10-on-success route, not a fixed-pay proposal. Found [an active-looking production webhook routing question](https://station.railway.com/questions/production-custom-domain-post-webhook-re-7448f71e) whose original poster shows zero replies and a $10 bounty. No evidence of an independently verified fix, no authorized current Railway Station posting session, and no acceptance; **did not claim/send**. Search results sometimes show *Solved* even with '0 Replies'; always read page status and payout rules before acting.
- [0penEx public board](https://0penex.com/) reported 230 listed opportunities (11 Superteam Earn, 169 Immunefi and 50 GitHub in snapshot). Source itself warns that Superteam amounts are shared prize pools, Immunefi amounts are maximum hypothetical security awards, and GitHub labels do not prove funding. This is **not 230 qualified cash jobs**. No Duet application submitted.
- First-party Superteam API `/api/listings?context=home&tab=Bounties&category=All`, and Development, Content, Other, Design variants: in the first 10 live entries from **each** category, every entry's `agentAccess` was `HUMAN_ONLY`. Do not enroll/substitute Duet for a human; this limited sample does not claim all platform listings are human-only.
- Superteam [projects vs. bounties FAQ](https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq): projects select a single freelancer; bounties are open competitions. Public page advertises a `Manual QA Tester - Sana.run Trading Terminal` $50-250 USDC project, but the actual listing details, agent eligibility, submission mechanism and available buyer assignment were not independently established via supported connected-account tools. Therefore **prospect only, not revenue or awarded contract**.
- [Superteam $200 Agentic Engineering Grant](https://superteam.fun/earn/grants/agentic-engineering/) explicitly shows **Applications Paused**, requires human verification, Solana application, coding subscription receipts and later proof of product shipment; not a zero-spend Duet pay source at present.
- [Algora's stale-bounty tracking problem](https://github.com/algora-io/algora/issues/213) has been publicly documented. Current advertised statuses can differ from GitHub, sponsorship may be conditional, and some listings have high claim saturation. Do not spend development effort on any without validating issue, payout and competition.

### Human micropayments (kept outside Duet revenue)

- [1Q official payments](https://support.1q.com/hc/en-us/articles/360057076311-How-are-respondents-paid): up to 25 cents per eligible question sent via phone app or SMS, PayPal promptly after response. [Official help](https://support.1q.com/hc/en-us/articles/360056656032-Why-didn-t-I-get-paid-for-answering-a-question) identifies missed deadlines and unpaid `Know` Freevert questions: *not every question pays*. Registration requires a real participant phone, email, and personal payout account, none authorized/accessed here. Frequency is not guaranteed.
- [Qmee U.S. FAQ](https://www.qmee.com/en-us/faq): PayPal/Venmo no-minimum withdrawal, but participant must take real surveys on their own account; rewards depend on provider qualification, no guarantee.
- [Prolific official AI use rule](https://participant-help.prolific.com/en/articles/445029-can-i-use-ai-assistance-tools-in-my-submission) forbids AI in responses unless specifically invited by the researcher. No compliant supported route to import 10 paid questions into chat was found. Do not fake respondent identity, copy proprietary survey material or invent earnings.
- Personal human survey payouts, if any, are *user earnings*. Subsequent optional investment into Duet is *owner capital*, never **independently earned Duet revenue**.

### Decision

No current candidate checked passed all gates: independent identified buyer, real funded scope, current assignment eligibility, supported project-account submission and verified payout without unauthorized cost. Preserve security and $0 spend. For another run, prioritize a **single approved exclusive buyer assignment** or confirmed authorized Railway help forum session. For personal cents, use genuine 1Q/Qmee manually rather than an agent impersonation workflow.
