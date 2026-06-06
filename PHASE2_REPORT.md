# Phase 2 Report — Autonomous, balanced coverage for SaaS builders

**Goal:** make `saas-builder` complete enough that a developer with only **Superpowers + saas-builder** installed can build a secure, well-designed, deployed digital product end to end — without needing Trail of Bits, codebase-audit-suite, ui-ux-pro-max, or anything else.

**Result:** the plugin went from **5 skills to 15** (10 new + 1 augmented). Every new skill is self-sufficient with an embedded fallback, works in English and Spanish, and targets the default stack **React + Vite + TypeScript + Vercel + Postgres**.

The phase opened with parallel research across 6 topic blocks (frontend quality, backend/architecture, applied security, DevOps, product/business, mobile). Each block returned reference repos with star counts, an existing-skill scan across marketplaces (obra/superpowers, anthropics, trailofbits, vercel-labs, expo), an A/B/C architecture recommendation, and embeddable methodology.

---

## Skills implemented

Architecture key: **A** = pure delegation · **B** = wrapper with embedded fallback · **C** = fully embedded.

| Skill | Category | Approach | Primary reference (⭐) |
| --- | --- | --- | --- |
| `secure-coding` | Security | C | OWASP Cheat Sheet Series (~29k), OWASP Top 10:2021, GDPR.eu |
| `auth` | Backend / Security | B | Better Auth (~28k), Clerk, Supabase Auth (~104k) |
| `api-design` | Backend | C | microsoft/api-guidelines (~23k), Stripe API docs, zod (~43k) |
| `data-modeling` | Backend | C | PostgreSQL RLS docs, supabase (~104k), AWS/PlanetScale tenancy guides |
| `payments` | Product / Business | B (hybrid) | stripe-samples (~800–900 each), Stripe MCP (~1.6k) |
| `deployment` | DevOps | C + B | GitHub Actions + Vercel docs, sentry-javascript (~8.5k) |
| `frontend-performance` | Frontend | C | GoogleChrome/web-vitals (~8.5k), web.dev, Vite docs |
| `technical-seo` | Product / Business | C | Google Search Central, react-helmet-async, vite-ssg |
| `accessibility` | Frontend | B | w3c/wcag 2.2, axe-core (~7k), vercel-labs/agent-skills (~27k) |
| `pwa` | Mobile | A + C | vite-plugin-pwa (~4k), Workbox (~13k); expo/skills for native |
| `ui-design` *(augmented)* | Frontend | C | style-dictionary (~4.7k), Tailwind v4, motion (~32k) |

**Why these approaches:**
- **C (embedded) dominates** because the value is opinionated, stack-specific methodology and decision rules, for which no authoritative installable skill exists (secure-coding, api-design, data-modeling, performance, SEO).
- **B (wrapper)** where a high-quality external resource exists but isn't universal: `auth` (delegates to a provider), `accessibility` (delegates the checklist to Vercel's skill + adds an axe-core runner), `deployment` (wraps Sentry setup).
- **A + hybrid** for `pwa` (canonical `vite-plugin-pwa`) and `payments` (delegates the Stripe *catalog* to the MCP, but **must embed** the Checkout-Session → webhook → fulfillment code, which the MCP cannot do).

`ui-design` was **augmented, not duplicated**: three-tier design tokens (Tailwind v4 `@theme`) and advanced responsive rules (container queries, fluid `clamp`, safe areas) were folded in, saving two skill slots for higher-value gaps.

---

## Skills investigated and discarded

| Candidate | Block | Reason for discard |
| --- | --- | --- |
| React Native / Expo skill | Mobile | Already solved by **`expo/skills`** (official, ~2k⭐, actively maintained by Expo). Needed only ~1 in 10 web-SaaS projects, post-PMF. `pwa` points users there for native. |
| Standalone "responsive design" skill | Mobile/Frontend | ~7 durable rules, not a workflow. **Folded into `ui-design`** instead — better triggering, no slot cost. |
| Standalone "design tokens" skill | Frontend | Overlaps `ui-design`'s existing system step. **Folded into `ui-design`** as the three-tier model. |
| Standalone "animations" skill | Frontend | Already partially in `ui-design` (MOTION_INTENSITY, Framer/Motion). Library choice, not a methodology gap. |
| `user-onboarding` skill | Product | Real value, but lower criticality than security/payments and overlaps `landing-page`/`ui-design` first-run UI. Deferred to Phase 3. |
| `product-analytics` skill | Product | Useful but not catastrophic-if-missing; instrumentation is a thin wrapper over PostHog. Deferred to Phase 3. |
| `realtime/websockets` skill | Backend | Needed only when a feature genuinely requires sub-second push; SSE-vs-WS decision can live as a note. Deferred to Phase 3. |
| Audit/scanner skill | Security | Out of scope — `secure-coding` is **prevention**; auditing is covered by separate audit plugins (Trail of Bits, codebase-audit-suite) the user can add. |
| GraphQL-specific skill | Backend | Folded into `api-design` as the "when to reach for it + N+1 guardrails" branch — the default is REST. |
| Env-config skill | Backend/DevOps | Split across `api-design` (zod validation at boot) and `deployment` (per-env scopes) — no standalone skill needed. |

**Priority criteria applied:** (1) how often a builder needs it per week, (2) whether a quality equivalent already exists in the ecosystem, (3) how catastrophic its absence is — weighted **security > performance/correctness > SEO/polish**. The 4 "flexible" slots (performance, SEO, a11y, PWA) were confirmed with the plugin owner; all four were selected, expanding the target from 8 to 10 new skills.

---

## Coverage: before vs after

| Category | Before (v1.0) | After (v2.0) |
| --- | --- | --- |
| Product discovery | ✅ `product-discovery` | ✅ unchanged |
| Architecture (high-level) | ✅ `architecture-primer` | ✅ unchanged |
| UI / design system | ✅ `ui-design` | ✅ + design tokens + responsive |
| Landing / marketing | ✅ `landing-page` | ✅ unchanged |
| API design | ❌ | ✅ `api-design` |
| Database / data modeling | ❌ | ✅ `data-modeling` |
| Auth & authorization | ❌ | ✅ `auth` |
| Applied security (prevention) | ❌ | ✅ `secure-coding` |
| Payments / monetization | ❌ | ✅ `payments` |
| Frontend performance | ❌ | ✅ `frontend-performance` |
| Accessibility | ❌ | ✅ `accessibility` |
| Technical SEO | ❌ | ✅ `technical-seo` |
| PWA / offline / mobile | ❌ | ✅ `pwa` (+ delegates native to expo/skills) |
| Deploy / CI/CD / monitoring | ❌ | ✅ `deployment` |
| Spanish-language routing | ❌ | ✅ `saas-router` (ES + EN) |

**Net:** the v1.0 plugin could *plan and design* a product but stopped before the backend. v2.0 covers the **entire lifecycle — plan → build → secure → monetize → polish → ship.**

---

## Reference repos used (full list)

| Repo / resource | ⭐ (approx) | URL |
| --- | --- | --- |
| donnemartin/system-design-primer | ~352k | https://github.com/donnemartin/system-design-primer |
| supabase/supabase | ~104k | https://github.com/supabase/supabase |
| colinhacks/zod | ~43k | https://github.com/colinhacks/zod |
| motiondivision/motion | ~32k | https://github.com/motiondivision/motion |
| OWASP/CheatSheetSeries | ~29k | https://github.com/OWASP/CheatSheetSeries |
| better-auth/better-auth | ~28k | https://github.com/better-auth/better-auth |
| nextauthjs/next-auth (Auth.js) | ~28k | https://github.com/nextauthjs/next-auth |
| vercel-labs/agent-skills | ~27k | https://github.com/vercel-labs/agent-skills |
| plausible/analytics | ~27k | https://github.com/plausible/analytics |
| PostHog/posthog | ~35k | https://github.com/PostHog/posthog |
| microsoft/api-guidelines | ~23k | https://github.com/microsoft/api-guidelines |
| gitleaks/gitleaks | ~18k | https://github.com/gitleaks/gitleaks |
| graphql/graphql-spec | ~14.6k | https://github.com/graphql/graphql-spec |
| graphql/dataloader | ~13.4k | https://github.com/graphql/dataloader |
| GoogleChrome/workbox | ~13k | https://github.com/GoogleChrome/workbox |
| GoogleChrome/web-vitals | ~8.5k | https://github.com/GoogleChrome/web-vitals |
| getsentry/sentry-javascript | ~8.5k | https://github.com/getsentry/sentry-javascript |
| dequelabs/axe-core | ~7k | https://github.com/dequelabs/axe-core |
| expo/expo | ~50k | https://github.com/expo/expo |
| react-navigation/react-navigation | ~24k | https://github.com/react-navigation/react-navigation |
| style-dictionary/style-dictionary | ~4.7k | https://github.com/style-dictionary/style-dictionary |
| vite-pwa/vite-plugin-pwa | ~4k | https://github.com/vite-pwa/vite-plugin-pwa |
| t3-oss/t3-env | ~4k | https://github.com/t3-oss/t3-env |
| OWASP/Top10 | ~4.5k | https://github.com/OWASP/Top10 |
| socketio/socket.io | ~63k | https://github.com/socketio/socket.io |
| expo/skills | ~2k | https://github.com/expo/skills |
| w3c/wcag | ~1.4k | https://github.com/w3c/wcag |
| stripe-samples/* | ~800–900 each | https://github.com/stripe-samples |
| nickcolley/jest-axe | ~1.1k | https://github.com/nickcolley/jest-axe |
| antfu-collective/vite-ssg | — | https://github.com/antfu-collective/vite-ssg |

Authoritative non-repo references: OWASP Top 10:2021, GDPR.eu / gdpr-info.eu (Art. 5, 32), Google Search Central, web.dev Core Web Vitals & Learn PWA, Vercel docs (env, instant rollback, rolling releases, image optimization), PostgreSQL RLS docs, AWS & PlanetScale multi-tenancy guides, Stripe docs (idempotency, Customer Portal, MCP).

---

## Gaps detected for Phase 3

Deliberately left out of Phase 2, with reasons:

1. **`user-onboarding`** — activation flows, empty states, first-run checklists, sample-data seeding. High product value; deferred because security/payments/correctness ranked higher and onboarding partially overlaps existing UI skills. **Strong Phase 3 candidate.**
2. **`product-analytics`** — instrument the AARRR funnel (activation, retention, MRR/churn) with PostHog + a swappable `track()` layer. Pairs naturally with onboarding.
3. **`realtime`** — SSE-vs-WebSocket decision, managed realtime on serverless, reconnection/backpressure. Only needed for a subset of products.
4. **`mobile-companion` (native)** — a thin skill that sets up the pnpm + Turborepo `packages/shared` boundary (types/API client) for an Expo app, then **delegates UI/build to `expo/skills`**. Not a full RN tutorial.
5. **Validation harness** — none of the 15 skills has an automated eval (skill-creator's benchmarking) confirming the `description` triggers reliably and doesn't collide with neighbors (e.g. `secure-coding` vs `auth`, `ui-design` vs `frontend-design`). Worth a Phase 3 triggering-accuracy pass.
6. **Worked end-to-end example** — a single reference repo built *by* the plugin (idea → deployed SaaS) would prove the chain holds and serve as documentation.
7. **Email/transactional** — sending (Resend/Postmark), templates, deliverability. Common SaaS need not yet covered.

**Recommendation for Phase 3:** prioritize `user-onboarding` + `product-analytics` (the "growth" layer) and the validation harness, since the build/secure/ship spine is now complete.
