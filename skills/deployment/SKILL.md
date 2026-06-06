---
name: deployment
description: This skill should be used when shipping an app to production — setting up CI/CD, deploys, preview environments, error monitoring, environment separation, or rollback. Trigger phrases include "deploy this", "set up CI/CD", "GitHub Actions", "add error tracking", "set up Sentry", "monitor production", "staging environment", "environment variables per environment", "how do I roll back", "preview deploys", "ship to production", "feature flags". It leans on what Vercel gives for free and adds only the missing pieces: a CI gate, Sentry, env hygiene, and a rollback plan.
---

# Deployment

This skill ships your app without over-building DevOps. The key insight: **Vercel already does ~80% of CI/CD and rollback for free.** The skill teaches what's free, then adds the thin layer Vercel doesn't give you.

Analogy: Vercel is a modern car with airbags, ABS, and a backup camera built in. You don't bolt on your own brakes — you learn the controls, then add the one thing it lacks (a dashcam, i.e. error monitoring).

## Discovery (max 3 questions, only if unknown)

1. Is the repo already connected to Vercel (or another host)?
2. Do you have automated tests / typecheck to gate merges on?
3. Do you need a separate staging environment, or are preview deploys enough?

## Step 1 — Deploys & previews (mostly free)

- **Connect the repo to Vercel once** via the dashboard. After that: every push to a non-main branch gets an automatic **Preview URL**; every merge to `main` auto-deploys **Production**. No `vercel deploy` in CI needed for the happy path.
- The **preview URL is your review environment** — reviewers test the real deployed build on each PR, not a local guess.
- Only script a CI-driven deploy (`vercel pull` → `vercel build` → `vercel deploy --prebuilt`) if you must deploy *after* CI in one pipeline, or for a non-connected repo. For a solo dev, native Git integration is less to maintain.
- **Backend / full-stack on InsForge:** if the backend lives on InsForge (see the `data-modeling` skill), the agent deploys edge functions, runs migrations, and can deploy the frontend through the `insforge-cli` skill — one place, agent-operated. Vercel still fits the frontend if you prefer the most-proven host; choose by the same *agentic-native vs mature-ecosystem* rule. **The CI gate, Sentry, env hygiene, and rollback steps below apply either way** — they're host-independent.

## Step 2 — Add a CI quality gate (the missing piece)

Create `.github/workflows/ci.yml` that runs on `pull_request`:

```yaml
on: pull_request
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run lint
      - run: npx tsc --noEmit
      - run: npm test
      - run: npm run build
```

- **Pin actions to a major tag** (`@v4`), never `@main` — reproducibility + supply-chain safety.
- **Enable branch protection** on `main`: require this workflow to pass before merge. That's what makes the gate real.

## Step 3 — Error monitoring (Sentry, with verified source maps)

- Install `@sentry/react` (runtime) and `@sentry/vite-plugin` (build-time source map upload).
- **Init early** in `src/main.tsx`, before render, with `dsn: import.meta.env.VITE_SENTRY_DSN`, `environment: import.meta.env.MODE`, and a `tracesSampleRate` (~0.1).
- **Readable stack traces require source maps**: set `build.sourcemap: true` and add `sentryVitePlugin({ org, project, authToken })` as the **last** Vite plugin. `SENTRY_AUTH_TOKEN` is build-time only — never `VITE_`-prefixed.
- **Alert on new + regression issues**, not every event (default alerting is noisy).
- **Verify once**: throw a deliberate error in a preview deploy and confirm a readable stack trace appears in Sentry.
- Free telemetry: `@vercel/analytics` + `@vercel/speed-insights` render in the root for pageviews + Core Web Vitals. Add an **UptimeRobot** check on the homepage for "whole site down" (which client-side Sentry can't report).

## Step 4 — Environment variables per environment

- Vercel gives **three scopes**: Development, Preview, Production. "Staging" = a Custom Environment or a branch-scoped Preview var.
- **`VITE_` is the security boundary** — only those vars reach the browser. Secrets must not carry it.
- Local: `.env.local` (git-ignored) + a committed `.env.example`. Mark secrets **Sensitive** (`vercel env add NAME production --sensitive`).
- **Keep variable names identical across envs**, change only values. `vercel pull --environment=preview` syncs them down; `vercel env ls` audits drift — the #1 cause of "works in preview, breaks in prod."

## Step 5 — Rollback plan

- **Instant Rollback is the default safety net** (zero setup): dashboard → pick a previous good prod deploy → re-aliases in seconds, no rebuild. CLI: `vercel rollback <id>`.
- **Gotcha**: after a rollback, prod auto-assignment is **off** — new pushes to `main` won't go live until you `vercel promote <good>`.
- **`git revert` is the durable fix** — rollback changes routing, not code; revert the bad commit so the next deploy is clean.
- **Risky launch?** Use Vercel **Rolling Releases** (staged %) or a **feature flag** (the `flags` SDK / OpenFeature) to ship code dark and flip it without redeploying. Decision: small bug → instant rollback + revert; risky launch → rolling release or flag.

## Output

Deliver: the `ci.yml`, branch-protection instructions, the Sentry init + Vite plugin config, the env-scope plan, and a written rollback runbook.

## Reference

actions/checkout + actions/setup-node, Vercel for GitHub / Instant Rollback / Rolling Releases docs, getsentry/sentry-javascript (~8.5k⭐), @sentry/vite-plugin, flags SDK / OpenFeature, InsForge deploy (agentic-native full-stack, via `insforge-cli`).
