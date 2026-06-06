---
name: data-modeling
description: This skill should be used when designing a database schema, modeling data, choosing a database, planning migrations, or setting up multi-tenancy for a SaaS. Trigger phrases include "design the database", "model this data", "what database should I use", "schema for", "multi-tenant", "tenant isolation", "add an index", "how do I migrate", "SQL or NoSQL", "Postgres schema", "row level security", "RLS". It defaults to Postgres, models multi-tenancy safely, and enforces migration and indexing discipline.
---

# Data Modeling

This skill designs the schema your product runs on, and gets multi-tenant isolation right — the mistake that, when wrong, leaks one customer's data to another.

Analogy: the schema is the foundation and load-bearing walls of a house. You can repaint and rearrange furniture later cheaply; moving a load-bearing wall after move-in is expensive and dangerous. Get the structure right before building on it.

## Discovery (max 3 questions, only if unknown)

1. Is this multi-tenant (multiple orgs/customers sharing the app) or single-tenant?
2. Is the data mostly relational (users, orders, invoices) or document-like/flexible?
3. Are you on Supabase, Neon, or another Postgres host — or undecided?

## Step 1 — Choose the database

**Postgres by default.** It covers relational integrity, JSONB for flexible fields, full-text search, and scales far. Don't reach for NoSQL without a proven document/scale reason.

- **Supabase** — batteries-included (Auth + RLS + Realtime + storage). Best default for a new SaaS.
- **Neon** — serverless Postgres with branching/autoscaling; great for preview-per-PR databases.
- Redis only for cache/sessions/real-time; Elasticsearch only for heavy full-text search.

## Step 2 — Model multi-tenancy (the critical decision)

**Default to a shared schema with a `tenant_id` (org_id) column on every tenant-scoped table + Row-Level Security.** Graduate to schema-per-tenant or DB-per-tenant **only** when a large enterprise customer demands hard isolation/compliance. Don't start there — it multiplies ops cost.

Make RLS airtight:
- `ENABLE ROW LEVEL SECURITY` **and** `FORCE ROW LEVEL SECURITY` on every tenant table.
- Set tenant context per request **inside the transaction**: `SET LOCAL app.current_tenant = '...'` — so pooled connections can't leak state between requests.
- The application DB role must have **neither `SUPERUSER` nor `BYPASSRLS`** — otherwise RLS is silently skipped and isolation is an illusion.
- RLS is the backstop for the app-layer `tenant_id` checks in the `auth` skill — defense in depth.

## Step 3 — Schema discipline

- **Normalize to 3NF by default.** Denormalize only for a *measured* read hot-path.
- **IDs**: UUID/ULID for public-facing identifiers; bigint identity for internal PKs.
- **Index every foreign key and every column you filter/sort/join on.** Postgres does **not** auto-index FKs. For tenant tables, lead a composite index with `tenant_id`, e.g. `(tenant_id, created_at)`.
- **Timestamps**: `created_at` / `updated_at` as `timestamptz` in UTC. Prefer **soft delete** (`deleted_at`) for user-facing data.
- **Push invariants into the schema**: `NOT NULL`, `CHECK`, `UNIQUE`, FK constraints — not just app code.

## Step 4 — Migrations

- All schema changes go through **versioned, forward-only migration files** in source control (Supabase migrations, Prisma Migrate, or Drizzle).
- **Never edit the production DB by hand.** Every change is a reviewable, replayable migration.
- For execution of SQL migrations + RLS on InsForge specifically, the `insforge-cli` skill handles the apply step; this skill owns the *design*.

## Handoff

The schema here backs the `api-design` resources and the `auth` permission model. Pass the tenant strategy to both so endpoints and policies scope correctly.

## Output

Deliver: the DB choice with reason, the multi-tenancy strategy, the table definitions (DDL) with constraints and indexes, the RLS policies if multi-tenant, and the first migration file.

## Reference

PostgreSQL docs (RLS, indexing), supabase/supabase (~104k⭐), AWS "Multi-tenant data isolation with Postgres RLS", PlanetScale "Approaches to tenancy in Postgres".
