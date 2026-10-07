# Deployment — field notes

From production apps on Vercel with a managed Postgres backend, most of them without a staging environment.

Format: **Symptom** → **Cause** → **Check**.

## Environment variables

**1. Nine of 37 production variables ended in a newline.**
- Cause: they were loaded with `echo "$value" | vercel env add`. `echo` appends `\n`. The dashboard does not show it.
- What broke: the payment SDK (its HTTP client rejected the header, so no request left the server) and every template string built from a base URL — the sitemap and `robots.txt` were split in the middle.
- What did not break: `fetch` (trims header whitespace) and `new URL()` (normalizes). That is why it went unnoticed.
- Check:
  ```bash
  vercel env pull out.txt --environment production
  grep '\\n"' out.txt     # each line is a contaminated variable
  ```
- Fix: load with `printf '%s' "$value" | vercel env add …`.

**2. The variable was fixed and nothing changed.**
- Cause: `NEXT_PUBLIC_*` / `VITE_*` values are inlined at build time. Changing one requires a rebuild, not a restart.

**3. Preview deploys had no database.**
- The backend variables existed only in Production, so previews rendered without login or data.
- That was left as is on purpose: the service key bypasses row-level security, and copying it to Preview hands it to every branch build. In a preview, test what does not need data; test the rest in production with the rollback ready.

**4. "Not authorized" with a valid session.**
- Cause: a missing team/scope flag on the CLI. Also pin the CLI version in scripts rather than `@latest`.

## Shipped is not the same as written

**5. The product took payments for weeks with its legal pages returning 404.**
- Cause: the files were written and committed; the site was never redeployed.
- Check: after any release, request the real URL. Verify against the domain, never against the disk.

**6. Server functions were older than the repo.**
- Cause: functions on a BaaS are deployed by a separate command; `git push` does not ship them.
- Check: compare the deployed function's source with the file in the repo as part of every release.

**7. An abandoned deploy kept publishing.**
- A forgotten project on another host was still building every push against a backend that no longer existed, serving a login that could never work — and its domain was still allowed in CORS and in the auth redirect list.
- Check: list every project connected to the repo, and every origin in CORS and auth settings.

## Releasing without staging

**8. Order of release.**
- Additive migration → code → restrictive migration. Code that expects a column must not ship before it exists; a restriction must not ship before the code stops relying on what it removes.
- Rehearse the migration inside `BEGIN … ROLLBACK` against production. One rehearsal caught a failing statement before it was applied.
- Write the rollback before you need it.

**9. A test user with a known password was linked to a real customer.**
- The password was in the repo; the customer had a real outstanding balance; the portal was already public.
- What held: tests that create their own data and throw-away credentials, clean up in `finally` (handling interruption too), and **verify the cleanup**. A cleanup that failed had been reporting success; its quoting was broken and it had never actually run.

**10. A test rewrote data for every customer.**
- A SQL test recalculated a score for all contacts; a bulk update moved `updated_at` and reordered every list. Scope tests to the rows they create.

## Serverless behavior

**11. Work started after the response was lost.**
- About 8% of a log was missing. The platform freezes the function once the response is sent. Use the post-response hook (`after()`, `waitUntil`).

**12. A monthly load could not run as a function.**
- 255 seconds and 197 MB against a 300-second limit. It runs on a server with a direct database connection.

**13. The scheduled job ran once a day.**
- Cause: the plan's cron limit. Moved to a database scheduler calling the same endpoint, with an idempotency flag.

**14. Two overlapping runs left a table half-loaded.**
- The job truncates and reloads. A lock file (`flock`) makes the second run exit.

## Network edges

**15. Every visitor appeared to be in the hosting provider's data center.**
- Cause: analytics proxied through a platform rewrite. The platform put its own egress IP in `X-Forwarded-For`; the visitor's address was in a platform-specific header. Seen in three projects.
- Related: a wrong script path returned an HTML page with status 200 and recorded nothing.

**16. Analytics were dead for 22 days.**
- Cause: a tightened Content-Security-Policy did not allow the analytics host. No error anywhere a person would look.
- Check: after any header change, confirm a visit is recorded.

**17. "Failed to fetch."**
- Twice it was CORS preflight, not the network: once a 404 on the preflight because the SDK derived the wrong functions subdomain, once a cross-origin POST to the apex domain, which redirects to `www` — preflights do not follow redirects.

## Builds

**18. Built locally, failed in CI.**
- Cause: a stray `@types/node` in a `node_modules` folder in the home directory was being resolved. Build in a clean checkout before trusting a local build.

**19. A major dependency upgrade returned 500 only when deployed.**
- An ESM-only package required from CommonJS. It worked in development.

**20. `npm audit fix --force` proposed downgrading the framework by many major versions.** Read what it will do.

## Backups

**21. Free plans pause and delete projects.**
- What held: a backup of the irreplaceable data on other infrastructure that **aborts if the export is empty**, restores without overwriting, and requires an explicit flag to run a restore. An export script must not replace a good backup with a failed one.
- Watch plan usage: one database was at 92% of its quota, and the next thing to fail would have been the load in the busiest week.
