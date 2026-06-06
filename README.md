# saas-builder

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/MartinOlivero/saas-builder)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

> Turn Claude Code into a product-building partner. Describe what you want to ship — a SaaS, a landing page, a dashboard, an MVP — and `saas-builder` asks the right questions, makes smart design and architecture decisions, and produces real, production-grade output instead of generic AI boilerplate.

`saas-builder` is a plugin for [Claude Code](https://claude.com/claude-code) (also compatible with Cursor, Codex, and OpenCode skills). It ships **five skills** orchestrated by a router that figures out what you're actually building before a single line of code is written.

## The problem it solves

Most AI coding help jumps straight to implementation. You ask for "a SaaS" and you get a purple-gradient, Inter-everywhere, no-empty-states UI built on a stack nobody chose on purpose. There's deep coverage in security and testing plugins — and almost nothing for **product design and architecture from scratch**. This plugin fills that gap: it does the thinking *before* the building.

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
You: "I want to build a SaaS for X"
        │
        ▼
   saas-router  ──►  asks 2-3 quick questions, then routes
        │
        ├─ landing page?      ──►  landing-page
        ├─ dashboard/admin?   ──►  ui-design (dashboard mode)
        ├─ full SaaS / MVP?   ──►  product-discovery ──► architecture-primer ──► ui-design
        ├─ architecture only? ──►  architecture-primer
        └─ loose UI work?     ──►  ui-design
```

The **router never lets Claude write code or design blindly.** It triages first — like a nurse sending you to the right specialist — then hands off with full context so you're never asked the same thing twice.

## The five skills

| Skill | Triggers on | What it does |
| --- | --- | --- |
| **`saas-router`** | "build me a…", "I want to create…", "design a…", any product request | The brain. Asks 2-3 questions and routes to the right specialist. |
| **`product-discovery`** | "I have an idea but…", "what should the MVP be?", "where do I start?" | Separates problem from solution, validates the market, defines a prioritized MVP (P0/P1/P2). |
| **`architecture-primer`** | "how do I structure this?", "monolith or microservices?", "what database?", "how does it scale?" | Discovery → decision tree → concrete decisions with trade-offs, stack, and a Mermaid diagram. Based on the System Design Primer. |
| **`ui-design`** | "design the UI", "pick colors", "create a design system", "dashboard layout" | Builds a design system *before* code. Tunable variance/motion/density. Bans the generic AI look. |
| **`landing-page`** | "build a landing page", "sales page", "page to sell X" | Proven section order + real copy + ready-to-use components. |

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
  → router → `product-discovery` → `architecture-primer` → `ui-design`
- **Landing page:** *"Build me a sales page for my online course about AI automation."*
  → `landing-page` (asks offer/avatar/CTA, generates copy + components)
- **Dashboard:** *"I need an admin dashboard to manage users and subscriptions."*
  → `ui-design` in dashboard mode (dense, data-first, all states handled)
- **Architecture decision:** *"Should I use a monolith or microservices for an app expecting 5,000 users?"*
  → `architecture-primer` (discovery → decisions with trade-offs → diagram)
- **Fuzzy idea:** *"I have an idea for an app but I'm not sure what to build first."*
  → `product-discovery` (problem first, then a scoped MVP)

## Why this plugin

There are plugins for almost everything *after* you've decided what to build — testing, security, refactoring, CI. There's a hole at the very start: **deciding what to build, how to architect it, and how to make it look like a real product.** `saas-builder` lives in that hole. It encodes the discipline of a good product partner — ask before assuming, scope before scaling, design before defaulting — so the output is something you'd actually ship.

## Credits

Created by **Martín Olivero / [IamAutom](https://iamautom.com)**.

`architecture-primer` is inspired by the [System Design Primer](https://github.com/donnemartin/system-design-primer). `product-discovery` draws on Design Sprint and Lean Startup.

## License

[MIT](./LICENSE)
