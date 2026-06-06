# saas-builder

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/MartinOlivero/saas-builder)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

> Turn Claude Code into a product-building partner. Describe what you want to ship — a SaaS, a landing page, a dashboard, an MVP — and `saas-builder` asks the right questions, makes smart design and architecture decisions, and produces real, production-grade output instead of generic AI boilerplate.

`saas-builder` is a plugin for [Claude Code](https://claude.com/claude-code) (also compatible with Cursor, Codex, and OpenCode skills). It ships **fifteen skills** orchestrated by a router that figures out what you're actually building before a single line of code is written — and then guides you across the whole lifecycle: discovery, architecture, backend, security, payments, polish, and deploy.

## The problem it solves

Most AI coding help jumps straight to implementation. You ask for "a SaaS" and you get a purple-gradient, Inter-everywhere, no-empty-states UI built on a stack nobody chose on purpose — with a string-concatenated SQL query, no rate limit, and a checkout that fulfills on the client redirect. This plugin does the thinking *before* the building, and bakes the safe default in *as* you build.

## Designed to be self-sufficient

`saas-builder` assumes you have **[Superpowers](https://github.com/obra/superpowers)** (brainstorming, TDD, debugging, planning, code review, git worktrees) and nothing else. It deliberately does **not** duplicate those. Everything else a solo developer needs to ship a professional digital product — secure backend, auth, payments, performance, accessibility, SEO, deploy — lives here, and every skill works standalone with an embedded fallback (it gets sharper when optional tools like `ui-ux-pro-max` or the Stripe MCP are present, but never blocks without them).

## Where it fits in your stack

`saas-builder` knows its lane. Process discipline comes from **Superpowers**; deep security *audit* and *fuzzing* come from optional review plugins (Trail of Bits, the testing handbook, audit suites). `saas-builder` owns the part those leave empty — **building the product itself**: design, architecture, backend, prevention-grade security, payments, and shipping.

If your setup already nails security and testing but has a hole in product design, architecture, and SaaS building, that hole is exactly what this fills:

| Lifecycle area | saas-builder | Who else / complement |
| --- | :---: | --- |
| Dev process — brainstorm, TDD, debug, git, review | `░░░░░░░░░░` | **Superpowers** owns this (not duplicated) |
| Product discovery & MVP scoping | `██████████` | — |
| Architecture & system design | `██████████` | — |
| UI/UX & design system | `██████████` | sharper with `ui-ux-pro-max` |
| Backend — API, data modeling, auth | `██████████` | InsForge / Supabase |
| Applied security — *prevention while building* | `██████████` | — |
| Payments & monetization | `██████████` | Stripe MCP |
| Performance · accessibility · SEO · PWA | `██████████` | — |
| Deploy · CI/CD · monitoring · rollback | `██████████` | — |
| Security *audit* & fuzzing | `░░░░░░░░░░` | Trail of Bits, testing-handbook *(optional)* |
| Codebase & docs audit | `░░░░░░░░░░` | codebase-audit-suite *(optional)* |

The takeaway: **Superpowers + saas-builder covers idea → shipped product.** Add audit/fuzzing plugins on top when you want a security review — they *grade* the house; `saas-builder` *builds* it (safely).

## What makes it different

Most AI coding tools act *after* a decision is already made — they review the code you wrote, scan the contract you deployed, or wrap one service and stop at its edge. `saas-builder` is opinionated about *when* it steps in. Two examples capture the whole philosophy.

### Security: prevention, not audit

The security ecosystem (Trail of Bits, Semgrep, CodeQL, audit suites) inspects **finished code** — it finds the SQL injection that's already there. Valuable, but late, and nothing stops you from *writing* the vulnerability in the first place. The `secure-coding` skill is that missing companion: it runs **while you build the endpoint**, baking in the parameterized query, the `zod` validation, and the server-side authz check before the bug can exist.

> It's the seatbelt you put on before driving — not the crash investigator who shows up afterward.

### Payments: the whole flow, not just the catalog

Stripe's own MCP is **control-plane only**: it creates products and prices, but it cannot create a Checkout Session or process a webhook. A plugin that merely wires the MCP gives you an app that *would sell but wouldn't charge* — the money never actually lands. The `payments` skill is deliberately hybrid: it delegates the catalog to the MCP, then **embeds the part that collects the money** — the Checkout Session → signature-verified webhook → idempotent fulfillment chain that Stripe's tooling leaves to you.

> The redirect is the customer saying "I'll pay." The webhook is the bank confirming the money arrived. You ship the product when the bank confirms — not on a promise.

### The pattern behind both

| Most AI tooling | saas-builder |
| --- | --- |
| Acts *after* the code is written (review, audit, scan) | Acts *while* you build — the safe default **is** the first draft |
| Point tools for one slice (a scanner, a UI kit, an MCP) | One coherent chain across the whole lifecycle |
| Wraps a service and stops at its edge | Delegates what's good, **embeds what the service can't do** |
| Generic output you fix later | Opinionated defaults tied to a real stack |

Every skill carries a one-line analogy like the two above — so you understand *why* a decision is right, not just copy it.

## Recommended design skills

`saas-builder` works standalone, but its design output gets sharper when the original design skills are present. The `ui-design` and `landing-page` skills delegate the design system to them when available and fall back to embedded principles otherwise.

### Auto-installed

- **taste-skill** → declared as a plugin dependency, installed automatically with `saas-builder` *when it is available as a Claude Code plugin*. It currently ships as a standalone skill rather than a marketplace plugin, so install it directly once:
  ```bash
  npx skills add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend"
  ```
  Provides the tunable style layer (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`). `saas-builder` uses it automatically once present.

### Manual install recommended

- **ui-ux-pro-max** (~87k ⭐): `npx uipro@latest init --ai claude`
  `saas-builder` detects whether it is installed and uses it automatically. If it is not installed, `saas-builder` uses embedded design principles as a fallback.

### How detection works

`saas-builder` checks for `ui-ux-pro-max` on every session start, via a `SessionStart` hook (`hooks/check-dependencies.sh`). If it is missing, you get a one-time install nudge; if it is present, the hook stays silent. Once installed, no further configuration is needed. The router and the architecture logic are fully independent and require nothing extra.

## How it works

```
You: "I want to build a SaaS for X"  (English or Spanish)
        │
        ▼
   saas-router  ──►  asks 2-3 quick questions, then routes
        │
  PLAN  ├─ fuzzy idea?        ──►  product-discovery
        ├─ architecture?      ──►  architecture-primer
        │
  BUILD ├─ database/schema?   ──►  data-modeling
        ├─ API/endpoints?     ──►  api-design
        ├─ login/roles?       ──►  auth
        ├─ UI / dashboard?    ──►  ui-design
        ├─ landing page?      ──►  landing-page
        │
  SECURE├─ any backend code   ──►  secure-coding  (runs throughout)
 MONEY  ├─ payments/billing?  ──►  payments
        │
 POLISH ├─ slow?              ──►  frontend-performance
        ├─ accessibility?     ──►  accessibility
        ├─ SEO / previews?    ──►  technical-seo
        ├─ offline/installable?──► pwa
        │
  SHIP  └─ deploy/CI/monitor? ──►  deployment
```

The **router never lets Claude write code or design blindly.** It triages first — like a nurse sending you to the right specialist — then hands off with full context so you're never asked the same thing twice.

## The fifteen skills

**Orchestration**

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`saas-router`** | "build me a…", "quiero construir…", any product request | The brain. Asks 2-3 questions and routes to the right specialist, in English or Spanish. |

**Plan & design**

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`product-discovery`** | "I have an idea but…", "what should the MVP be?" | Separates problem from solution, validates the market, defines a prioritized MVP (P0/P1/P2). |
| **`architecture-primer`** | "how do I structure this?", "what database?", "how does it scale?" | Discovery → decision tree → decisions with trade-offs, stack, Mermaid diagram. Based on the System Design Primer. |
| **`ui-design`** | "design the UI", "pick colors", "dashboard layout" | Design system *before* code: three-tier tokens, responsive rules, tunable variance/motion/density. Bans the generic AI look. |
| **`landing-page`** | "build a landing page", "sales page" | Proven section order + real copy + ready-to-use components. |

**Build the backend**

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`api-design`** | "design the API", "REST or GraphQL?", "an endpoint" | REST conventions (errors, pagination, idempotency, versioning), REST-vs-GraphQL decision, env-config validation with zod. |
| **`data-modeling`** | "design the database", "schema for…", "multi-tenant" | Postgres by default, safe multi-tenancy (`tenant_id` + RLS), indexing and migration discipline. |
| **`auth`** | "add login", "user roles", "JWT or sessions?", "SSO" | Picks a provider (Clerk/Supabase/Better Auth) over rolled-your-own; sessions-vs-JWT, RBAC, multi-tenant scoping. |

**Secure & monetize**

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`secure-coding`** | writing any endpoint/input/data write, "is this secure?", "rate limit" | OWASP Top 10 as *prevention* rules, input validation, mass-assignment guard, secrets hygiene, GDPR basics — baked in as you build. |
| **`payments`** | "add Stripe", "subscriptions", "pricing", "billing" | Correct Stripe flow (Checkout → webhook → fulfill), customer portal, idempotent fulfillment, sane pricing tiers. |

**Polish & ship**

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`frontend-performance`** | "make it faster", "Core Web Vitals", "bundle too big" | Hits LCP/INP/CLS targets with Vite chunking, `React.lazy`, image/font fixes, CI bundle budget. |
| **`accessibility`** | "make it accessible", "a11y", "WCAG", "screen reader" | WCAG 2.2 AA: semantic HTML, keyboard/focus, accessible forms, contrast, `jest-axe` in CI. |
| **`technical-seo`** | "improve SEO", "meta tags", "no preview on WhatsApp" | Per-page OG/Twitter tags, sitemap/robots, JSON-LD, and the SPA-prerender fix so crawlers actually see your content. |
| **`pwa`** | "make it a PWA", "work offline", "push notifications" | Installable + offline with `vite-plugin-pwa`, the right caching strategy, and the stale-service-worker fix. |
| **`deployment`** | "deploy this", "CI/CD", "Sentry", "rollback" | Uses what Vercel gives free, adds a GitHub Actions CI gate, Sentry with source maps, env hygiene, and a rollback runbook. |

## Installation

This repository doubles as its own Claude Code marketplace, so installation is two commands:

```bash
/plugin marketplace add MartinOlivero/saas-builder
/plugin install saas-builder
```

Then restart or reload, and the skills activate automatically based on what you ask for.

**Try it locally without installing** (for development):

```bash
claude --plugin-dir /path/to/saas-builder
```

## Example prompts

Each of these activates the right skill on its own — you don't call skills by name.

- **Full SaaS:** *"I want to build a SaaS that helps freelancers track invoices."*
  → router → `product-discovery` → `architecture-primer` → `data-modeling` → `api-design` → `auth` → `ui-design`
- **Landing page:** *"Build me a sales page for my online course about AI automation."*
  → `landing-page` (asks offer/avatar/CTA, generates copy + components)
- **Dashboard:** *"I need an admin dashboard to manage users and subscriptions."*
  → `ui-design` in dashboard mode (dense, data-first, all states handled)
- **Backend:** *"Design the database for a multi-tenant project tracker."*
  → `data-modeling` (Postgres, `tenant_id` + RLS, indexes, first migration)
- **Auth:** *"Add login with Google and admin roles."*
  → `auth` (provider pick + RBAC + protected routes)
- **Security, while building:** *"Add an endpoint to update a user's profile."*
  → `secure-coding` (zod `.strict()` validation, authz check, mass-assignment guard)
- **Payments:** *"Add Stripe subscriptions with a monthly and annual plan."*
  → `payments` (Checkout → webhook → idempotent fulfillment + customer portal)
- **Performance:** *"My app's Lighthouse score is bad and the bundle is huge."*
  → `frontend-performance` (Vite chunking, lazy load, CWV targets)
- **SEO:** *"My SaaS has no preview when shared on WhatsApp/Twitter."*
  → `technical-seo` (OG tags + SPA prerender so crawlers see them)
- **Ship it:** *"Set up CI and deploy to production with error tracking."*
  → `deployment` (GitHub Actions gate + Sentry + rollback runbook)
- **Fuzzy idea:** *"I have an idea for an app but I'm not sure what to build first."*
  → `product-discovery` (problem first, then a scoped MVP)

## Why this plugin

There are plugins for almost everything *after* you've decided what to build — testing, security, refactoring, CI. There's a hole at the very start: **deciding what to build, how to architect it, and how to make it look like a real product.** `saas-builder` lives in that hole. It encodes the discipline of a good product partner — ask before assuming, scope before scaling, design before defaulting — so the output is something you'd actually ship.

## Reference sources

Each skill encodes methodology from authoritative, community-validated sources:

| Skill | Built on |
| --- | --- |
| `architecture-primer` | [System Design Primer](https://github.com/donnemartin/system-design-primer) (~352k⭐) |
| `product-discovery` | Design Sprint, Lean Startup |
| `api-design` | [microsoft/api-guidelines](https://github.com/microsoft/api-guidelines) (~23k⭐), Stripe API + idempotency docs, [zod](https://github.com/colinhacks/zod) (~43k⭐) |
| `data-modeling` | PostgreSQL RLS docs, [supabase](https://github.com/supabase/supabase) (~104k⭐), [insforge](https://github.com/insforge/insforge) (~5k⭐, agentic-native), AWS + PlanetScale multi-tenancy guides |
| `auth` | InsForge Auth (agentic-native), [Better Auth](https://github.com/better-auth/better-auth) (~28k⭐), [Auth.js](https://github.com/nextauthjs/next-auth) (~28k⭐), Clerk, Supabase Auth |
| `secure-coding` | [OWASP Cheat Sheet Series](https://github.com/OWASP/CheatSheetSeries) (~29k⭐), OWASP Top 10:2021, [GDPR.eu](https://gdpr.eu), [gitleaks](https://github.com/gitleaks/gitleaks) (~18k⭐) |
| `payments` | [stripe-samples](https://github.com/stripe-samples), Stripe Customer Portal docs, Stripe MCP, InsForge Stripe integration (agentic-native) |
| `frontend-performance` | [GoogleChrome/web-vitals](https://github.com/GoogleChrome/web-vitals) (~8.5k⭐), web.dev, Vite build docs |
| `accessibility` | [w3c/wcag](https://github.com/w3c/wcag) 2.2, [axe-core](https://github.com/dequelabs/axe-core) (~7k⭐), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (~27k⭐) |
| `technical-seo` | Google Search Central, react-helmet-async, [vite-ssg](https://github.com/antfu-collective/vite-ssg) |
| `pwa` | [vite-plugin-pwa](https://github.com/vite-pwa/vite-plugin-pwa) (~4k⭐), [Workbox](https://github.com/GoogleChrome/workbox) (~13k⭐), [expo/skills](https://github.com/expo/skills) (native) |
| `deployment` | GitHub Actions + Vercel docs, [sentry-javascript](https://github.com/getsentry/sentry-javascript) (~8.5k⭐), InsForge deploy (agentic-native, via `insforge-cli`) |
| `ui-design` | [style-dictionary](https://github.com/style-dictionary/style-dictionary) (~4.7k⭐), Tailwind v4, [motion](https://github.com/motiondivision/motion) (~32k⭐) |

## Credits

Created by **Martín Olivero / [IamAutom](https://iamautom.com)**.

## License

[MIT](./LICENSE)
