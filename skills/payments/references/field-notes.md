# Payments — field notes

From production apps charging through Stripe and Mercado Pago: a paid community, a B2B tool sold by subscription, a CRM.

Format: **Symptom** → **Cause** → **What held**.

## The customer paid and got nothing

**1. The first real customer paid and no account was created.**
- Cause: the subscription event arrived with `payer_email: ""`. The code used `??`, which only falls back on null or undefined — an empty string passed through. The email was on a different object: the payment, not the subscription.
- What held: `||` for "empty or missing", and knowing which object carries each field. With Mercado Pago subscriptions that meant looking up the authorized payment and then the payment itself.
- Rule: **an empty field is not an absent field, and the sandbox will not show you which you will get.**

**2. Checkout and the billing portal were dead; the error said "connection".**
- Cause: the secret key had a trailing newline, added by `echo "$value" | <cli> env add`. The Stripe SDK uses Node's `http` module, which rejects the header before the request leaves the server.
- How to tell: a wrong key with a newline gives a *connection* error; the same wrong key, clean, gives an *authentication* error — meaning it reached Stripe. If you see a connection error, suspect the variable before the network.
- What held: `printf '%s'` when loading secrets, and a defensive `.trim()` where the client is created. See the `deployment` field notes for detection.

**3. `success_url` was invalid.**
- Cause: the same newline, this time inside a base URL used in a template string.

## Sandbox and real money

**4. The payment sandbox could not be made to work.**
- Mercado Pago requires both buyer and seller to be test users; two attempts failed.
- What held: a real plan at the minimum amount, in production.

**5. A test charged real money.**
- Cause: a live access token stored under a variable name containing "TEST".
- What held: check the token's prefix before saving it, and again at startup.

**6. A simulated event answered the wrong question.**
- "Does the event include the payer's email?" could only be answered by a real payment. See note 1.

## Subscriptions over time

**7. People who verified their email late arrived with the trial already expired.**
- Cause: the access rule measured `created_at + 7 days`. Meanwhile a scheduled job kept emailing them invitations to a trial they could not use. It affected 2 of 9 activations.
- The wrong diagnosis came first, from a database in which no profile was currently trialing — the condition was never checked against a live case.
- What held: an explicit `trial_ends_at` set at activation, and the access rule reading that.

**8. A failed renewal locked the customer out while the provider was still retrying.**
- What held: a grace state — access continues, with an email — while the provider reports a retry in progress; `past_due` only when it gives up.

**9. Resubscribing left two subscriptions.**
- What held: cancel the previous one at the provider when a new one is created.

**10. Renewals reset the customer's password.**
- Risk caught before it shipped: the provisioning function sent fresh credentials on every event. An idempotent "create account" must do nothing the second time.

**11. Cancellation could not find the account.**
- Cause: the cancellation event does not carry the email.
- What held: store the provider's customer/subscription id against the user at sign-up, and subscribe to both the payment and the subscription events.

**12. Ad platforms were told about sales that did not happen.**
- Cause: a conversion was reported on every webhook; the provider sends one for each change to the subscription.
- What held: report when the account is created, once.

## Webhook integrity

**13. The signature never verified.**
- Cause: the hosting gateway parsed and re-serialized the JSON before the function saw it.
- What held: use the event only as a notification and fetch the object from the provider's API. See the `integrations` skill, Step 1.

**14. An older event overwrote a newer state.**
- Design that came out of it: apply states idempotently and discard any event older than the last one applied. Carry your user id in `client_reference_id`.

**15. Do not rename metadata keys that are already stored at the provider.** Old subscriptions keep the old keys forever; keep a written list of the legacy names your webhook must still accept.

## Who is asking

**16. Anyone could open another customer's billing portal.**
- Cause: the endpoint identified the user from a readable, unsigned cookie.
- What held: validate the session token with the auth provider on the server. See the `auth` field notes.

## Pricing display

- Two buttons with two amounts read as two plans, even when one is "monthly" and one "annual" of the same plan.
- A bare "$" does not say which currency. In a market with more than one, write it.
