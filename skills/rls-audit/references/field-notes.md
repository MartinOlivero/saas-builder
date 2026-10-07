# RLS audit — field notes

Failures found in production SaaS apps. Every one of them had RLS enabled, a passing build and passing tests. None was found by a scanner.

Format: **Symptom** (what could be done) → **Cause** → **Check** (how to find it in your app).

## Rows are protected, columns are not

**1. A new user made themselves super-admin of another organization.**
- Symptom: one `PATCH` to their own profile row set `role` and `org_id`.
- Cause: the update policy was "you may edit your own row". Nothing said which columns.
- Check: for every table a user can update, try to change each privileged column on your own row with the public key.

**2. A customer turned their order into a credit note.**
- Symptom: changing one `kind` column kept the goods and created a credit for the same amount. They could also insert lines carrying their own `customer_id` and another customer's `order_id`.
- Cause: every policy compared `customer_id`, a column the customer writes.
- Fix that held: the `UPDATE` policy was deleted outright instead of listing forbidden columns — the forbidden list had already been one item short.

**3. A customer could read the supplier's cost on every line.**
- Symptom: `unit_cost` came back in the API response; the margin was computable from the console.
- Cause: the UI hid the column; RLS let the row through whole.
- Fix: a view projecting only the safe columns. Column-level `REVOKE` was not possible there because customers and staff shared one Postgres role.

**4. Any member could read another member's OAuth access token.**
- Cause: tokens stored in a tenant-readable table.
- Check: grep the schema for `token`, `secret`, `key`, `cost`, `*_id` of payment providers. Each needs to be unreadable from the API roles.

**5. Users picked their own matchmaking tier; members read payment-provider ids.**
- Same shape in two more apps: a rating column was editable and billing ids were readable because the row was "theirs".
- Fix in both: `revoke` the table-level privilege, then `grant update (…)` / `grant select (…)` on the safe columns only, and name columns explicitly in client queries.
- The pattern appeared in four separate projects. Assume it is in yours.

## Born open

**6. An anonymous `UPDATE` on a view changed the products table.**
- Cause: three things stacked — default privileges gave `anon` full rights on every new object, the view was auto-updatable, and it ran as an owner with `BYPASSRLS`. Four policies on the base table were never consulted.
- Check: `pg_default_acl`, then every view's `reloptions` and owner.

**7. Paid content was readable with the public key.**
- Cause: nine tables carried `*_select_all` policies (`USING (true)`, role public) that appeared in no migration in the repo. Nobody on the team had written or reviewed them.
- Check: diff `pg_policies` against the migrations folder.

**8. Leads of every organization were readable for three months.**
- Cause: eight `anon … true` policies had been added so an incoming webhook could write. The integration was removed; the policies were not.
- Check: list every policy that names `anon` and name the feature that needs it.

**9. A debugging table stayed public.**
- Cause: a `webhook_debug` table created to diagnose a third party, RLS never enabled, readable with the public key.
- Check: every table without RLS, especially ones created in a hurry.

## Functions that skip the lock

**10. Any caller could create a team member with any role in any organization.**
- Cause: a `SECURITY DEFINER` function took `role` and `org_id` as parameters and checked neither.

**11. An anonymous caller spent another organization's quota.**
- Cause: the guard compared the caller's role, which was `NULL` for anonymous. The comparison was neither true nor false, so the guard never raised.

**12. With someone else's uuid, you saw their calendar.**
- Cause: a `SECURITY DEFINER` function trusted a tenant id parameter; `EXECUTE` was never revoked from `PUBLIC`.
- Fix: `SECURITY DEFINER` was removed — the function did not need it, and as an ordinary function RLS applies. Ask of each one whether it needs the privilege at all.

**13. Fourteen server functions enforced a weaker rule than the app.**
- Cause: each read the user's organization directly and none checked that the user was active or the subscription current — the app did. Two doors, two rules.
- Fix: one SQL gate function, plus a test that compares server permission with screen permission across every role combination.

**14. A server function read `org_id` from the request body.**
- Cause: it queried with the service key, so RLS never ran, and the tenant came from the caller.

## Tests that were green and proved nothing

**15. The access test passed while the function was down.**
- Cause: a 404 "function not found" also leaves the row count unchanged.

**16. A security test targeted a case that could never fail; another never checked that login had succeeded.**
- Practice that came out of it: run every new test against the unfixed code and watch it fail.

**17. A locked-content wall never rendered.**
- Cause: RLS hid the locked rows, so the UI had nothing to show a lock on — the upsell was dead for months. At the same time a paying member could read the video URLs of the higher plan.
- Fix: split by what each table is for. The catalog table (title, cover, lesson count) became readable by every signed-in user; the content table stayed closed and gained the plan check. If the UI must show "locked", RLS cannot hide the row — and the lock icon is not the access control.

## Small things that were real

- After adding columns, the API returned a schema-cache error until `NOTIFY pgrst, 'reload schema'`.
- A role check queried memberships with no filter and took the first row: any reader passed as admin, and the audit log attributed the action to someone else. Filter by the caller's id — never ask "does an admin exist?".
- A helper function created only for tests was `SECURITY DEFINER` and shipped as a migration. Test helpers do not go into migrations and are not exposed through the API.
