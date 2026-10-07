# API design — field notes

From production apps whose "API" is a mix of server routes, edge functions and a BaaS SDK called from the browser.

Format: **Symptom** → **Cause** → **What held**.

## Errors that do not throw

**1. Failures nobody saw, for days.**
- Many SDKs return `{ data, error }` and never throw. Unchecked, the failure is invisible:
  - AI spend was not recorded when an insert hit a unique constraint, so the daily cap never saw it.
  - Emails rejected by the provider were indistinguishable from sent ones.
- This was the most common reason a bug took days to notice.
- What held: check `error` on every call — or wrap the client once so it throws — and treat an unchecked result as a lint failure.

**2. A read error was treated as "does not exist".**
- An accept-invitation function discarded the error from reading the profile, concluded the user had no organization, and moved them out of the one they had.
- Rule: "could not read" and "not found" are different results. Only the second may trigger a create.

## Retries

**3. A retried order was duplicated. It took four rounds to fix.**
- Round one: the retry created the order again.
- Round two: the order was reused but its lines were inserted twice.
- Round three: the pending id was lost when the user switched tabs — and the error message sent them to that tab.
- Round four: clearing the id when the cart was emptied reopened the duplicate.
- What held: before re-inserting, ask the server whether the order already has lines; keep the pending id outside the component that unmounts.
- Rule: **"the response was lost" is not "it was not saved".**

**4. A paid action ran twice.**
- Two simultaneous requests both passed a check that only looked at completed work. Reserve first (see `ai-features`, Step 4).

## Writes

**5. Editing a product's price reset its stock.**
- Cause: the form sent every field, including the stock value it had loaded when the screen opened. Movements in between were overwritten without an error.
- Rule: send only the fields the user changed.

**6. Points were awarded twice.**
- Cause: a database trigger granted them and the client also called an endpoint to grant them. That endpoint could be called repeatedly with no cap.
- What held: one writer, on the server, with daily caps enforced in the database.
- The same shape elsewhere: a payment record was created as `verified` by the client, skipping approval.
- Rule: rewards, credits, balances and payment states are written in exactly one place, and the client is not it.

## Reads

**7. 103 ids in a query string returned a gateway error.** Over 3,500 characters. Chunk `in (…)` filters (40–100 per request).

**8. A list stopped at 1000 rows without saying so.** Auto-generated APIs cap page size. Paginate with a stable order.

**9. A destructive action took the first search result.** The search matched partially. Filter for exact equality before deleting or updating.

## Telling the truth in the response

**10. A gateway error became an empty list.**
- The screen then stated "0 of 5 online". Return `null` (unknown) and let the UI say "could not check". See `ui-design`, honest states.

**11. "Nothing was changed" on a 502.**
- For a call to a third party, a 5xx or timeout means *unknown*. See `integrations`, Step 2.
