---
name: technical-seo
description: This skill should be used when making a web app or SaaS discoverable and shareable — meta tags, OpenGraph/social previews, sitemap, robots.txt, structured data, or fixing the empty-HTML problem of a React SPA. Trigger phrases include "improve SEO", "add meta tags", "OpenGraph", "social share preview", "sitemap", "robots.txt", "structured data", "JSON-LD", "my page has no preview on Twitter/WhatsApp", "Google can't see my SPA", "prerender". It generates the head tags, files, and prerendering an SPA needs to be indexed and shared.
---

# Technical SEO

This skill makes a SaaS findable by Google and shareable on social — and fixes the specific trap of a Vite SPA serving near-empty HTML that crawlers can't read.

Analogy: an SPA is a book with a blank cover and blank first page until you open it and read aloud. Search crawlers and social bots only glance at the cover — if it's blank, they walk away. SEO here is printing a real cover (server-rendered head tags) so they see what the book is about.

## The SPA problem (state it upfront)

A Vite SPA serves near-empty HTML; content and meta tags appear only after JS runs. Social crawlers (WhatsApp, Twitter, LinkedIn) **don't run JS at all**, so share previews need tags that are **injected server-side or prerendered** — client-only `react-helmet` alone won't show a preview on WhatsApp.

**Be precise about Google, though.** Googlebot does render JavaScript: for one production SPA, Search Console's URL inspection showed the fully rendered page indexed. So do not migrate frameworks *for Google alone* — check your own site in Search Console first. What remains true: rendering is deferred, social bots never run JS, and you should not assume AI crawlers do. Prerender the public routes for those reasons.

## Discovery (max 3 questions, only if unknown)

1. Which pages need SEO — public marketing/landing/pricing, or also app routes?
2. Is the broken thing indexing (Google) or social previews (no image on share)?
3. Can you prerender marketing routes to static HTML, or must it stay a pure SPA?

## Step 1 — Per-page head tags

Use `react-helmet-async` to set per route: unique `<title>`, `<meta name="description">`, a canonical link, and **OpenGraph + Twitter Card** tags:

- `og:title`, `og:description`, `og:image` (1200×630), `og:url`, `twitter:card=summary_large_image`.
- Always **absolute URLs** in `og:image`/canonical (relative URLs break previews).
- Set `<html lang>` and one canonical per page to avoid duplicate-content issues.

## Step 2 — Make crawlers actually see them (the high-impact fix)

- **Marketing/landing routes → prerender to static HTML** with `vite-ssg` (or React SSR). Crawlers get real content + OG tags in the initial response. This is the single highest-impact change.
- **Pure CSR SPA, OG tags only → the "OG proxy" pattern**: a Vercel function + `vercel.json` rewrite that detects social/bot user-agents and serves HTML with the correct meta injected.

## Step 3 — Ship the crawl files

- **`robots.txt`** in `/public`: allow crawl of public routes, block private/app routes, and point to the sitemap (`Sitemap: https://domain.com/sitemap.xml`).
- **`sitemap.xml`** generated at build time (via `vite-ssg` output or a sitemap plugin), listing public URLs with `<lastmod>`. Submit it in Google Search Console.

## Step 4 — Structured data (JSON-LD)

Add `<script type="application/ld+json">` blocks:
- `Organization` + `SoftwareApplication`/`Product` on home/pricing.
- `FAQPage` on FAQ sections.
- `BreadcrumbList` where relevant.
Validate with Google's Rich Results Test.

## Step 5 — Performance is SEO

Core Web Vitals feed ranking. Hand off to the `frontend-performance` skill: code-split routes, lazy-load below-the-fold images, serve modern image formats, keep third-party scripts async/minimal.

## Field notes — check the live output, not the code

Each of these shipped past a green build:

- **No `robots.txt` or `sitemap.xml` at all**, no canonical tag, and `lang="en"` on a Spanish site. Request the files; read the `<html>` tag.
- **A sitemap split in the middle of every URL** and a broken `Sitemap:` line — the base URL came from an environment variable with a trailing newline. Open the sitemap in a browser.
- **Apex → `www` answered 307** instead of a permanent redirect.
- **The social image rendered with the system font** because it was generated from a `file://` page where the web font never loaded. Look at the actual image.
- **A font subset fell back silently**: only `latin-ext` was loaded, and that subset does not contain the basic Latin characters — it extends `latin`, it does not include it.
- **Analytics proxied through a rewrite located every visitor in a data center** (see `deployment` field notes).

Verify ownership by domain in Search Console and submit the sitemap there; it is also the only reliable way to see what Google actually rendered.

## Output

Deliver: the `react-helmet-async` head component with OG/Twitter tags, the prerender or OG-proxy setup, `robots.txt`, the sitemap generation step, and the JSON-LD blocks for the key pages.

## Reference

Google Search Central docs, react-helmet-async, antfu-collective/vite-ssg, Vercel functions / `vercel.json` rewrites.
