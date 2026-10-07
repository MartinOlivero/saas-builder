# Secure coding — field notes

Holes found in production apps that had authentication, RLS and a passing test suite. For database permissions specifically, see the `rls-audit` field notes.

Format: **Symptom** → **Cause** → **What held**.

## The client decided something it should not

**1. A customer could save an order line at any price.**
- Cause: the server checked who owned the line, not where the price came from.
- What held: the server sets price, cost and total. The client sends the product and the quantity.

**2. Any signed-in user could overwrite another user's avatar or a course cover.**
- Cause: the storage path came from the form, and the upload ran with the admin client. That admin client had been introduced earlier to make an "invalid token" error go away.
- What held: the server builds the path — under `<user_id>/` for user content — picks the bucket, rejects SVG, caps the size.
- Rule: **switching to the admin client to silence a permission error removes the permission.** Find out why the user's own token was refused.

**3. A server endpoint trusted a cookie the browser could edit.**
- See the `auth` field notes, note 3.

## Public endpoints (no login)

A public booking form in production ended up with all of these, each added after a specific problem:

- **A captcha that fails open** — a doubtful booking is better than a lost lead — but only when its health check returns a real 2xx. The proxy in front answered 502 even with the service down, so "any response" was not a valid health signal.
- **Captcha assets served from your own origin**, not a CDN.
- **A honeypot field with a name autofill will not touch.** The first one was filled by the browser's autocomplete and rejected real people.
- **A cap per organization**, because the platform did not reliably expose the visitor's IP.
- **Restricted characters in the visitor's name.** It ended up in the title of a calendar invitation sent from a trusted address — so it must not be able to carry a domain, even written with spaces.
- **Escaped wildcards** (`%`, `_`) in a pattern search on email.
- **An id generated up front** for the record, matching the id the calendar provider would use, so the provider's webhook could not create a duplicate.

## Content-Security-Policy that actually holds

- **Removing `'unsafe-inline'` in Next.js requires a per-request nonce.** The framework emits several inline scripts of its own per page; they cannot be moved to files. Generate the nonce in the middleware, send the CSP on the request (the framework reads it there to tag its scripts) and on the response.
- **Declare the CSP in one place.** With one in the config and one in the middleware, the browser enforces both.
- **`'strict-dynamic'`** lets nonce-tagged scripts load their own dependencies and makes host allowlists unnecessary.
- **Leave `style-src` without a nonce** if you use libraries that set inline styles: once a nonce is present, the browser ignores `'unsafe-inline'` there.
- **Allow `'unsafe-eval'` only in development.** Check the production bundle for `eval(` and `new Function(` first.
- **Try a stricter policy with `Content-Security-Policy-Report-Only`** in production: it reports without blocking.
- **`font-src 'self'` blocks hosted web fonts silently** — the app renders in the system font and nothing errors. Self-host the fonts.
- **Detect violations with the `securitypolicyviolation` DOM event.** The console API does not surface them to automation. Before trusting "zero violations", trigger one on purpose to confirm the detector works.
- **After any change, confirm your own analytics still records.** A stricter policy silently disabled measurement for three weeks.

## Secrets

**4. An API key was published inside a Markdown file.**
- Cause: `git add -A`. The key was in a notes file nobody thought of as code.
- What held: stage files by name. Keep secrets outside the repository tree entirely, not merely ignored.

**5. A live API key sat in a troubleshooting document, and webhook secrets in a "backup" JSON.**
- Docs, exports and debug dumps are where secrets end up. Scan `docs/`, `*.md` and `*.json` — and the history — not only source files.

**6. Automation-tool nodes held the admin key as a plain parameter.**
- In those tools, credentials are encrypted and node parameters are not. Six nodes had it.

**7. Test scripts with the service key were found in three separate repositories.**

**8. A test account's password was committed — and the account was linked to a real customer.**

## Smaller ones that were real

- A shared-secret check for a scheduled endpoint must reject an empty value and compare in constant time.
- A redirect parameter accepted external URLs. Accept only paths that start with a single `/`.
- A demo account open to visitors is an attacker-controlled tenant. See `multi-tenancy`, Step 7.
