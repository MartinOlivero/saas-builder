---
name: saas-router
description: This skill should be used FIRST whenever the user wants to create, build, design, ship, or prototype any digital product — a SaaS, web app, platform, MVP, landing page, sales page, dashboard, admin panel, backoffice, internal tool, API, database, auth, payments, or any user interface. Trigger phrases (English) include "build me a", "I want to create", "design a", "let's make a", "I have an idea for", "help me ship". Trigger phrases (Spanish) include "quiero construir", "armar una", "diseñar una", "hagamos un", "tengo una idea para", "necesito una app/SaaS/landing", "agregá login/pagos/base de datos", "subir a producción". It routes the request to the correct specialist skill instead of writing code or designing blindly.
---

# SaaS Router

This skill is the brain of the saas-builder plugin. It runs before any product work and decides which specialist skill should handle the request.

## The one rule that cannot be broken

**Do NOT write code, design a UI, or pick a stack before routing through this skill.** Jumping straight to implementation is the most common failure mode — it produces generic output that ignores what the user actually needs. Route first, build second.

Analogy: this is the triage nurse at a hospital. Nobody goes straight to surgery. The nurse asks two or three quick questions, then sends the patient to the right specialist.

## Workflow

### Step 1 — Ask 2-3 quick routing questions

Do not interrogate. Ask only what is needed to classify the request. Pick from:

- "What are you building — a landing page, a dashboard, or a full app/SaaS?"
- "Do you already know exactly what it should do, or are you still shaping the idea?"
- "Is there an existing product/codebase, or are we starting from zero?"

If the user's first message already answers these (e.g. "build me a pricing landing page for my course"), skip straight to routing — do not re-ask what is already known.

### Step 2 — Route to the right specialist

Match the request (English **or** Spanish) against this table and activate the matching skill. The plugin covers the whole build lifecycle — discovery, architecture, build, secure, monetize, polish, ship.

**Plan & design**

| User says / wants | Route to |
| --- | --- |
| "SaaS", "platform", "app", "MVP", "product" / "idea para", idea not fully defined | `product-discovery` → `architecture-primer` → build skills → `ui-design` |
| "architecture", "how do I structure this", "scale", "what stack" / "cómo lo estructuro", "qué stack" | `architecture-primer` |
| "landing", "sales page", "lead capture" / "página de ventas", "captar leads" | `landing-page` |
| "dashboard", "admin", "backoffice", "internal tool" / "panel", "tablero" | `ui-design` (dashboard mode) |
| Any UI/UX, component, colors, design system / "diseñá", "componente", "que se vea bien" | `ui-design` |

**Build the backend**

| User says / wants | Route to |
| --- | --- |
| "design the API", "endpoint", "REST or GraphQL" / "diseñar la API", "un endpoint" | `api-design` |
| "database", "schema", "model this data", "multi-tenant" / "base de datos", "modelar los datos" | `data-modeling` |
| "login", "auth", "roles", "permissions", "SSO" / "agregar login", "roles", "permisos" | `auth` |

**Secure & monetize**

| User says / wants | Route to |
| --- | --- |
| Writing any endpoint / input / data write, "is this secure", "rate limit", "secrets" / "esto es seguro", "manejar datos de usuarios" | `secure-coding` (runs alongside backend work) |
| "payments", "Stripe", "subscriptions", "pricing", "billing" / "cobrar", "suscripciones", "precios" | `payments` |

**Polish & ship**

| User says / wants | Route to |
| --- | --- |
| "slow", "performance", "Core Web Vitals", "bundle size" / "está lento", "optimizar" | `frontend-performance` |
| "accessible", "a11y", "WCAG", "screen reader", "keyboard" / "accesibilidad" | `accessibility` |
| "SEO", "meta tags", "social preview", "sitemap" / "que Google lo encuentre", "preview en WhatsApp" | `technical-seo` |
| "PWA", "installable", "offline", "push notifications" / "que funcione offline", "instalable" | `pwa` |
| "is this safe to ship", "pre-launch security check", "did I miss anything", before deploying / "antes de subir, ¿está seguro?" | `pre-ship-security` |
| "deploy", "CI/CD", "GitHub Actions", "Sentry", "rollback", "staging" / "subir a producción", "monitoreo" | `deployment` |

### Step 3 — Hand off with context

When routing, pass along everything already learned so the specialist does not re-ask. State the handoff explicitly, e.g. "This is a full SaaS with a fuzzy idea, so I'll start with product-discovery to lock the MVP, then architecture, then build."

## The full-SaaS lifecycle

A from-scratch SaaS runs through these phases. Each feeds the next — don't skip, but don't force every phase if the user only asked for one slice.

1. **`product-discovery`** — define the problem, the user, and the MVP scope.
2. **`architecture-primer`** — decide the high-level system design and stack.
3. **Build** — `data-modeling` (the schema) → `api-design` (the endpoints) → `auth` (who can do what) → `ui-design` (the interface). **`secure-coding` runs throughout**, not as a final step.
4. **Monetize** — `payments` when it's time to charge.
5. **Polish** — `frontend-performance`, `accessibility`, `technical-seo`, `pwa` as the product matures.
6. **Ship** — `pre-ship-security` for a final security review of the finished code, then `deployment` for CI/CD, monitoring, and rollback.

Building UI before the MVP is defined, or picking a stack before knowing the scale, produces rework. But `secure-coding` is never deferred — preventing a vulnerability is always cheaper than auditing one out later.

## When NOT to route

If the user explicitly asks for one specific thing ("just give me a Tailwind navbar"), honor it and go straight to `ui-design`. Routing serves the user — it is not a toll booth. Use judgment: ambiguity means ask; clarity means act.
