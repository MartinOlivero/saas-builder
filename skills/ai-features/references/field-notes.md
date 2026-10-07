# AI features — field notes

What actually happened in production apps that call a model on behalf of their users: a sales bot on a messaging platform, a call-auditing feature inside a CRM, a lead-qualifying assistant.

Format: **Symptom** → **Cause** → **What held**.

## Money

**1. Two simultaneous requests were both billed.**
- Cause: the duplicate check looked only at saved reports. Neither had been saved yet.
- What held: take a turn in the database before calling the model.

**2. Every click on "Retry" charged again.**
- Cause: the function hit its time limit after the model had answered; the screen said "interrupted".
- What held: a timeout on the call itself, retry only on request, and a record that the paid work exists.

**3. The plan quota lived in the browser.**
- What held: the counter is incremented by the same server function that makes the call.

**4. A paid report was not counted when the page reload failed.**
- Cause: the count happened in a client step after the call.

**5. The bot went down with a payment-required error.**
- Cause: one aggregator account shared by several projects ran out of credit. A separate workspace did not separate the balance.
- What held: one account per product, low-balance alert.

**6. About 8% of responses had no cost record.**
- Cause: the record was written after the HTTP response was sent, on serverless; the platform froze the function.
- What held: the platform's post-response hook.

**7. Cost came from the orchestrator's estimate.**
- What held: the provider's `usage` figure; a missing figure stored as NULL, never as 0.

**8. No limit at all.**
- 300 inbound messages were 300 calls. Caps by day, by hour per sender and in money were added, with a single notice and a switch to manual handling when reached.

Measured for scale: auditing a 76-minute call transcript with a small model cost about US$ 0.023. The risk is not the unit price; it is the missing ceiling.

## Invention

**9. "The batteries are lithium."** They were gel; the product record did not state the type. The bot also invited a customer to "come try them" at a store with no test units and offered cash payment at an online checkout.
- What held: an explicit "what is not in the record, you do not know" rule, and for each new data field a list of what must not be inferred.

**10. A lead's summary used another lead's name.** The model was handed a table and wrote about the wrong row.
- What held: code selects the row; the model only writes about the one it is given.

**11. "Cost per sale" was reported with no ad spend.**
- What held: the number is computed in code; if it cannot be computed it is not in the prompt.

**12. The string `"false"` counted as true; quotes were accepted when they matched inside a longer word.**
- What held: parse and validate every field before saving.

**13. A classifier ignored its instructions because of one line of context.**
- The prompt said to disregard "no vehicle on file". It routed to sales anyway, three times out of three. Removing the line fixed it.

## Things the model treats as optional

**14. 3 buying signals recorded out of 106 real messages.** A customer who asked for bank details was still marked "cold".
- Cause: recording the signal was a tool call with no effect on the reply.
- What held: a database trigger with rules tested against the real messages (the first rule set had two false positives), filtered so the bot's own messages were not scored.

**15. The contact's name was saved two times out of three.**
- Cause: the prompt referred to tools by names that no longer existed after a migration. Aligned names: five out of five.

## Failure

**16. The provider was overloaded and the customer got nothing.** No trace was left either; the owner noticed because they happened to be watching.
- What held: an honest notice, an error event with the real cause, hand-off to a person, and a window so the apology is not repeated.

**17. "0 of 5 agents online."**
- Cause: a gateway error was turned into an empty list. "Could not find out" was rendered as "zero".

**18. Four outages attributed, in turn, to provider load, the timeout, and prompt length.**
- Actual cause: structured-output mode with a schema of twenty fields; the model emitted whitespace until it ran out of tokens. With production parameters, 17 of 18 identical calls got stuck.
- What held: the same schema requested as a forced tool call — 12 of 12 good. The fix was confirmed by repeating the identical request, not by one success.
- The lesson inside the lesson: nobody had repeated the call to see whether it was slow or stuck until the fourth outage.

**19. Four out of five calls failed with HTTP 200.**
- Cause: an aggregator chose a different upstream provider per call; the ones without structured-output support returned the error inside a 200 body. Asking it to "require the parameters" was not enough.
- What held: pinning the upstream provider. Separately, a reply cut at the token limit came back with `content: null`.

## Tests

**20. The test against the real API stayed green while production was broken.**
- Cause: the test built its own request instead of importing the production function.

**21. The suite checked the switch, not the light.** It asserted the pause flag; nothing asserted that a reply was sent.

## Conversations

- Replying to each short message made the bot repeat questions. Waiting six to eight seconds and answering only the latest fixed it, and cut a messaging bill that charged per reply.
- A pre-classifier ("doorman") call before the main call cost an extra request and split the conversation's context. It was removed.
- Retrieval does not shrink instructions: it replaces data, not rules.
