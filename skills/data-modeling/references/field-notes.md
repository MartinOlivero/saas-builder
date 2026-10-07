# Data modeling — field notes

From production apps on Postgres behind an auto-generated API: an ordering portal with stock and balances, a lead system, a paid community, a CRM.

Format: **Symptom** → **Cause** → **What held**.

## Invariants belong in the database

**1. A product's stock went to −420.**
- Cause: the lines of a shipped order were deleted before the order. The only thing preventing it was a hidden button.
- What held: triggers tied to the state transition, and corrections made by a compensating movement — never by deleting history.

**2. A payment lost its owner.**
- Cause: deleting a customer set the foreign key to null (`ON DELETE SET NULL`).
- What held: `ON DELETE RESTRICT` on anything that is money.

**3. A customer could order 500 units at 1.**
- Cause: the policy checked whose line it was, not where the price came from.
- What held: a trigger sets price, cost and total; the client sends product and quantity.

## One writer per field

**4. A streak counter never increased.**
- Cause: two code paths wrote the same "last active" date. The first to run made the second exit early with "already active today".
- What held: deleting one writer. A state field has exactly one.

**5. A bot's pause flag ended up inverted.**
- Cause: the "is the bot paused" decision depended on two fields written by different paths. The bot either talked over the salesperson or never came back.

## Pending needs an expiry

**6. A proposed match that nobody confirmed blocked the user for the week.**
- What held: a scheduled job cancels proposals whose time has passed.

**7. Offers were never closed.**
- Cause: the function that expires them existed and nothing called it.
- Rule: every "pending", "proposed", "paused" or "reserved" state needs a deadline, something that enforces it, and a UI that shows it.

## Concurrency

**8. Two simultaneous webhooks created two leads for one customer.**
- What held: a partial unique index (tenant, phone) over open leads. Uniqueness under concurrency is a database constraint, not a check in code.

**9. A returning customer stayed unassigned forever.**
- Cause: `INSERT … ON CONFLICT DO NOTHING` collided with an old, expired row and silently did nothing.
- What held: `ON CONFLICT DO UPDATE … WHERE status <> 'pending'`.
- Related trap: the upsert then took a row lock and deadlocked with a job that locked the same rows in the opposite order. Pick one lock order.

**10. Detect conflicts by code, not by message.** Matching the text "duplicate" was replaced by SQLSTATE `23505`.

## Dates

**11. A dashboard showed zero.**
- Cause: a job shifted the dates but not the derived "month" column the dashboard filtered by. Derived columns must be recomputed with their source — or be generated columns.

**12. Tests passed or failed depending on the time of day.**
- Cause: fixtures built from "now plus an interval", and date helpers that used the process's time zone.
- What held: run the suite with the time zone forced, and fix the clock in tests.

**13. Evening activity fell into the next day.**
- Cause: periods cut at UTC midnight. A day is a concept in the tenant's time zone.

See `multi-tenancy` for time zone as tenant data.

## Reads

**14. 61 rows meant 61 requests, and the page fell over.**
- What held: one view using `DISTINCT ON` to return the latest related row per parent.

**15. The database accepted 30 connections; ten concurrent requests to one endpoint used them up.**
- Know your plan's connection limit before load does.

## Schema history and backups

**16. The backend project was lost and rebuilt from a two-month-old export.**
- The export had no primary keys (twelve were reconstructed by hand), truncated long statements (three policies were cut), exported no sequences, and omitted tables linked to the auth schema.
- Rule: version the schema as migrations from the first day, and **restore a backup once before you need to**. An export you have never restored is not a backup.

**17. A migration half-applied.**
- Cause: the runner did not stop at the first error. `\set ON_ERROR_STOP on`, and never edit a migration that has been applied.

**18. Inserts failed after tightening grants.**
- Cause: privileges on sequences were revoked along with the tables. Roles that insert need `USAGE` on the sequence.

## User-supplied files

**19. The first row of an import vanished.**
- Cause: the file had no header and the parser assumed one. Detect it — if the first row holds a valid identifier, it is data — and have the user confirm ambiguous columns.
