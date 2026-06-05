---
name: saas-router
description: This skill should be used FIRST whenever the user wants to create, build, design, ship, or prototype any digital product — a SaaS, web app, platform, MVP, landing page, sales page, dashboard, admin panel, backoffice, internal tool, or any user interface. Trigger phrases include "build me a", "I want to create", "design a", "let's make a", "I have an idea for", "help me ship". It routes the request to the correct specialist skill instead of writing code or designing blindly.
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

Match the request against this table and activate the matching skill:

| User says / wants | Route to |
| --- | --- |
| "landing", "sales page", "home page", "lead capture", conversion-focused page | `landing-page` |
| "dashboard", "panel", "admin", "backoffice", "internal tool", data-heavy UI | `ui-design` (dashboard mode) |
| "SaaS", "platform", "app", "MVP", "product" (idea not fully defined) | `product-discovery` → then `architecture-primer` → then `ui-design` |
| "architecture", "how do I structure this", "how does it scale", "what stack" | `architecture-primer` |
| Any UI/UX, component, or visual work with no broader context | `ui-design` |

### Step 3 — Hand off with context

When routing, pass along everything already learned so the specialist does not re-ask. State the handoff explicitly, e.g. "This is a full SaaS with a fuzzy idea, so I'll start with product-discovery to lock the MVP, then architecture, then UI."

## The full-SaaS chain

A from-scratch SaaS runs through three skills in order. Each feeds the next:

1. **`product-discovery`** — define the problem, the user, and the MVP scope.
2. **`architecture-primer`** — decide the system design and stack for that MVP.
3. **`ui-design`** — build the interface on top of the decided stack.

Do not skip steps. Building UI before the MVP is defined, or picking a stack before knowing the scale, produces rework.

## When NOT to route

If the user explicitly asks for one specific thing ("just give me a Tailwind navbar"), honor it and go straight to `ui-design`. Routing serves the user — it is not a toll booth. Use judgment: ambiguity means ask; clarity means act.
