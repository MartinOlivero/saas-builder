---
name: ui-design
description: This skill should be used when making visual design decisions, creating components, defining styles, colors, typography, spacing, or building any interface — including dashboards, admin panels, and web apps. Trigger phrases include "design the UI", "build a component", "pick colors", "create a design system", "make it look good", "style this", "dashboard layout", "make a dark mode". It generates a design system before writing code and avoids generic AI aesthetics.
---

# UI Design

This skill produces distinctive, production-grade interfaces. It orchestrates a UI/UX-pro approach with deliberate taste: decide the design system first, then write code that expresses it.

Analogy: an architect does not start laying bricks. They draw the blueprint — materials, proportions, palette — and only then build. The design system is the blueprint.

## Workflow

### Step 1 — Identify the product type

The product type drives the entire visual language. Classify first: fintech, edtech, e-commerce, SaaS, health, dev tool, social, creative, internal/dashboard, etc. A health app and a crypto exchange should never look the same.

### Step 2 — Generate the design system BEFORE writing code

Define and state these explicitly:

- **Visual style** — pick one with intent: glassmorphism, minimalism, brutalism, bento grid, neo-retro, editorial, etc. Justify it against the product type.
- **Color palette** — primary, secondary, neutrals, and semantic colors (success / warning / error / info). Defined as tokens, not ad-hoc hex.
- **Typography** — a heading font, a body font, and a mono font (for code/numbers). Avoid defaulting to Inter for everything.
- **Spacing and border radius** — a consistent scale (e.g. 4/8/12/16/24) and a radius decision (sharp, soft, or pill).
- **Dark mode** — decide yes or no up front; if yes, define the dark tokens now, not later.

### Step 3 — Apply to the user's stack

Default stack: **React + Vite + Tailwind + shadcn/ui**. Supported alternatives: Next.js, Vue, Svelte, plain HTML + Tailwind. Ask which one if unknown; otherwise use the default and say so.

### Step 4 — Tune the three design parameters

Expose and set these 1-10 dials, and let the user adjust:

- **DESIGN_VARIANCE (1-10)** — from centered, safe layouts (1) to asymmetric, expressive compositions (10).
- **MOTION_INTENSITY (1-10)** — from simple hover states (1) to scroll-driven and orchestrated animations (10).
- **VISUAL_DENSITY (1-10)** — from airy, spacious layouts (1) to compact, information-dense dashboards (10).

**Dashboard mode:** when building a dashboard, admin, or backoffice, bias VISUAL_DENSITY high (7-9), keep DESIGN_VARIANCE moderate (data clarity over expression), and prioritize legible tables, filters, empty/loading/error states, and scannable hierarchy.

### Step 5 — Respect the forbidden anti-patterns

Never ship these:

- **The AI default look:** Inter + purple gradient + heavy rounded cards. It screams "generated." Avoid it.
- **Magic colors:** no raw hex values scattered in markup. Every color comes from the system tokens.
- **Ignored states:** never deliver a UI without designing the empty, loading, and error states. They are part of the work, not an afterthought.

## Output

Produce **ready-to-use components**, not throwaway prototypes — wired to the design tokens, with all states handled.

## Key landing components

When building landing or marketing pages, the standard component set is: **hero, navbar, features, pricing, testimonials, CTA, footer**. (For full landing structure and copy, the `landing-page` skill drives the flow and calls this skill for the visual system.)
