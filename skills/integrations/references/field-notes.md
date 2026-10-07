# Integrations — field notes

Observed while integrating production apps with a scheduling service, a CRM platform, an ERP's API, a messaging platform, payment providers and an email service.

Format: **Symptom** → **Cause** → **What held**.

## Webhooks

**1. The webhook was registered and never fired.**
- Eight tests over two days; the fault was on the provider's side.
- What held: a "sync now" button that pulls. A five-minute poll was rejected because it does not scale per tenant.

**2. The fix for that outage weakened security twice.**
- A debug table created to inspect payloads was left readable with the public key.
- A later change made the handler skip signature verification when the signature header was absent.
- Diagnostic shortcuts are the changes most likely to be forgotten. List them when you add them.

**3. A gateway re-serialized the JSON body and the signature never matched.**
- What held: stop trusting the body. Use the id, fetch the object.

**4. One message from an unregistered number silenced every other tenant.**
- Cause: an early `return` inside the loop over entries of a batched webhook.
- Earlier, an exception in one message left the previous ones saved and unanswered.
- What held: `try/catch` per item, persist before enqueueing, `continue` instead of `return`.

**5. "Cancelled" turned into "Rescheduled".**
- Cause: the app's own update came back through the provider's webhook and overwrote the result.

**6. Two simultaneous webhooks split one customer into two leads.**
- What held: a partial unique index in the database — not a check in code.

## Writing to someone else's system

**7. Rescheduling gave the appointment to another person.**
- Cause: the update omitted the assignee, and the provider re-ran its own distribution.

**8. The user retried and the customer got two notifications.**
- Cause: a gateway error was shown as "nothing was changed".

**9. An appointment moved three hours.**
- Cause: a datetime without an offset.

**10. The response had `appointment` where the documentation said `event`.**

**11. The provider rejected return URLs containing its own brand name.**

## Reading from someone else's system

**12. 44% of revenue was missing from an import, including the largest customer.**
- Cause: the endpoint returned `has_more: false` with 33 records pending.
- Earlier, another endpoint ignored `limit` and only 9% of purchases had been downloaded.
- What held: stop on an empty page; reconcile the total against the provider's own report.

**13. A date filter returned records from another month.**
- The count looked right. Comparing ids exposed it.

**14. 61 parallel requests brought the page down; then 103 ids in one URL returned a gateway error.**
- What held: a single query for the first, chunks of 40 for the second.

**15. A cron silently processed only the first 1000 rows.**
- Cause: the auto-generated API's row cap, with no error.

## Credentials

**16. A token with a 60-day life.** Weekly renewal job with an email alert on failure.

**17. Single-use refresh token, two processes.** A database lock so only one renews.

**18. New permissions, old installations.** Every existing install returned 401 until reinstalled.

**19. "Connected", but nothing synced.**
- Cause: the user left the calendar scope unticked on the consent screen. The app never checked which scopes were granted.

**20. "Disconnect" deleted the row and kept the grant.** The privacy policy promised otherwise.

**21. Asking for an extra scope switched the user's account.**
- Cause: a new sign-in was started instead of linking the identity; the chosen provider account did not match.

## Tests that lied

**22. The bot was down for six minutes and a button had been broken since it was built.**
- Cause: a header name with one letter wrong. The resulting 403 had been read as "the guard works".

**23. Months of analytics located every visitor in the hosting provider's data center.**
- Cause: a rewrite to an external origin replaced the forwarded-for header with the platform's egress IP. The analytics vendor's own documentation was wrong about which header to read; it was settled with an echo container.
- Same integration: a wrong script path returned HTML with status 200 and measured nothing.

**24. The sandbox contact was a plausible personal email address.**
- All writes were stopped until it was replaced with an owned address. The sandbox tool also needed guards: a missing argument still sent an update to the real record.

**25. A payment sandbox could not answer the only question that mattered.**
- "Does the subscription event include the payer's email?" It did not — and only a real payment showed that.

## Smaller ones

- A CDN in front of an API blocked the default user agent of an HTTP library with a 403 that looked like bad credentials. Seen with two unrelated providers.
- A messaging platform changed its pricing unit; the bot went from about 2.5 messages per reply to one.
- After moving logic from an automation tool to an API route, a failure of the new endpoint left the customer with no reply and no record that they had written.
- Email provider SDKs return `{ error }` instead of throwing. Rejected sends were indistinguishable from delivered ones until the return value was checked.
