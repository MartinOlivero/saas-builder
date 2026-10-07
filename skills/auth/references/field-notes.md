# Auth — field notes

From production apps on managed auth (BaaS providers), mostly Next.js and React SPAs.

Format: **Symptom** → **Cause** → **Check**.

## The guard that was not guarding

**1. A redirect to `/login` carried the whole page in its body.**
- Symptom: `curl` on a protected route, with no session, returned 307 — and 441 KB of conversations, phone numbers and emails.
- Cause: the only check was in the layout. The framework renders layout and page in parallel, so the page's data was already in the response.
- Check: request every protected route with `curl` and no cookies. Look at the **size of the body**, not the status code.
- Rule: the guard goes in the middleware (or the equivalent that runs before rendering).

**2. The middleware never ran.**
- Cause: the file sat at the project root in a project that uses a `src/` directory. The framework ignored it silently.
- Check: the same `curl` test. A middleware you have not seen reject a request is not known to exist.

**3. Anyone could act as any user on one endpoint.**
- Cause: the server read the user from a readable, unsigned cookie holding JSON.
- Rule: a cookie you can read and edit is not identity. The server validates the session token with the auth provider on every request that matters.

## Sessions across domains

**4. Users were bounced to login on Safari.**
- Cause: the backend lives on another domain, so its refresh cookie is a third-party cookie, which Safari blocks. Any browser that blocks third-party cookies behaves the same.
- What held: the SDK mode that sends the refresh token in the request body instead of a cookie. Also: the CSRF token had to be stored before the app started, or the first refresh invalidated the session.
- Check: test sign-in, wait past the access-token lifetime, and reload — in Safari.

**5. A storm of 401s.**
- Cause: a helper that refreshed the session ran before every query and did not remember that it had just failed.
- Rule: every refresh attempt has a cap and a memory.

**6. Coming back to an idle tab showed empty pages.**
- Cause: the token had expired; the fetches failed with no error handling.
- What held: re-fetch when the tab becomes visible again.

## Empty is not the same as nothing

**7. Blank screens, no error.**
- Cause: the session cookie was alive but the SDK had no tokens. The middleware let the request through, every query ran as anonymous, and RLS returned empty lists. `/login` then redirected back to the app.
- A direct link to an item said "not found", because the query ran before the token was ready.
- Rule: wait for the session before querying, and sign the user out if the server does not confirm it. A list emptied by RLS looks exactly like a list with no data.

## Logging out

**8. Logout did nothing, quietly.**
- Cause: the SDK sent the request without the CSRF token, got a 403, and swallowed it in an empty `catch`.
- And after a successful logout, the old refresh token kept issuing access tokens for seven days — stateless tokens with no rotation.
- Check: log out, then replay the old refresh token from the command line. If it still works, logout is cosmetic; say so in your threat model and shorten the lifetime.

## OAuth

**9. Signing in with a provider bounced back to login.**
- Cause one: the callback returned to a protected route, and the middleware redirected before the code was exchanged. The callback must be a public route that performs the exchange.
- Cause two: the session cookie was set too late for the next request. It was written explicitly in the callback.

**10. After signing out, the next sign-in went straight into the previous account.**
- What held: `prompt=select_account`.

**11. The post-login redirect accepted any destination.**
- What held: accept only a path that starts with a single `/`. Apply it to every `redirect`/`next` parameter.

## Account lifecycle

**12. Deleting one account nearly deleted another.**
- Cause: the provider's user search matched partially — `x@gmail.com` also returned `x@gmail.com.ar` — and the code took the first result. Caught by mutating the test before the first real deletion.
- Rule: before any destructive action, filter the result for exact equality.

**13. Every forgotten password went through a person.**
- Cause: no SMTP configured, so no recovery email. Configure sending before the first external user.

**14. Email verification was off in production.** Turn it on before launch; it is usually off by default in development setups.

## Role checks

**15. The role came from the first row returned.**
- A membership query with no filter returned every visible row; the code used the first. Filter by the caller's id. See `rls-audit`.
