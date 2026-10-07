---
name: payments
description: This skill should be used when adding payments, subscriptions, billing, or pricing to a SaaS — Stripe integration, checkout, plans, the customer portal, webhooks, or deciding a pricing model. Trigger phrases include "add Stripe", "accept payments", "add a subscription", "charge users", "pricing tiers", "checkout", "billing portal", "handle the webhook", "set up plans", "monetize", "free trial". It wires Stripe correctly (checkout to webhook to fulfillment) and sets a sane pricing model.
---

# Payments

This skill turns an app into a SaaS that actually collects money — and does it without the classic bugs (fulfilling on the client redirect, double-granting access, unverified webhooks).

Analogy: the checkout redirect is the customer saying "I'll pay." The **webhook** is the bank confirming the money arrived. You ship the product when the bank confirms, not when the customer promises. Trusting the redirect is shipping on a promise.

## The Stripe MCP split (read this first)

A Stripe MCP may be available (`mcp__stripe__*`). It is **control-plane only**: it creates products, prices, and payment links, and reads/updates subscriptions and customers. It **cannot** create Checkout Sessions or process webhooks.

So the architecture is hybrid:
- **Delegate the catalog to the MCP** — use it to create products, prices, and one-off **payment links** (the lowest-effort path for an MVP).
- **Embed the integration code** — Checkout Session creation, the webhook handler, and fulfillment must live in your shipped code, because the MCP can't do them.

If no MCP is present, create the catalog by hand in the Stripe dashboard or via the SDK; everything else below is identical.

**Backend delegation:** if you're on **InsForge** (see the `data-modeling` skill), its `insforge` / `insforge-cli` skills wire Stripe checkout, subscriptions, the customer portal, and the webhook handler for you — let them own the plumbing. The **rules below still hold regardless** (fulfill only on the webhook, verify the signature, stay idempotent); InsForge automates the wiring, it doesn't change what "correct" means. On Vercel/Node you write the handler yourself as shown. Never block on a missing skill.

## Discovery (max 3 questions, only if unknown)

1. One-time payments, subscriptions, or both?
2. Do you want the fastest path (hosted Checkout) or a fully custom in-page card form (Elements)?
3. What's the backend for the webhook — Vercel functions, a Node server, or a BaaS?

## Step 1 — Pick the integration

- **Default: Stripe Checkout (hosted).** Fastest, PCI-lightest. Reach for **Elements** only when you need a custom in-page card form.
- **Zero-backend MVP**: a **Payment Link** (creatable via `mcp__stripe__create_payment_link`) needs no code at all.

## Step 2 — The correct flow (Checkout → webhook → fulfill)

1. **Create the Checkout Session server-side** (e.g. `/api/checkout`): pass `mode: 'subscription'` (or `'payment'`), the `price` ID, `success_url`, `cancel_url`, and `client_reference_id` = your app's user id. Redirect the browser to `session.url`. The secret key never touches the client.
2. **Fulfill ONLY on the `checkout.session.completed` webhook** — never on the success redirect. A user can hit `success_url` without paying; the webhook is the source of truth.
3. **Verify the webhook signature**: `stripe.webhooks.constructEvent(rawBody, sig, endpointSecret)`. On Vercel you must read the **raw body** (disable body parsing) or verification fails.
4. **Make fulfillment idempotent** — Stripe retries webhooks; key on `event.id` or the subscription id so double-delivery doesn't double-grant access.
5. **Store `stripe_customer_id` and `stripe_subscription_id`** on the user row.

## Step 3 — Subscribe to the events that matter

- `checkout.session.completed` → provision access.
- `customer.subscription.updated` / `.deleted` → plan change / cancel.
- `invoice.paid` / `invoice.payment_failed` → renewals and dunning.

## Step 4 — Self-serve billing

Use the **Customer Portal**: create a Billing Portal Session server-side and redirect. Let Stripe handle upgrades, cancels, and card updates instead of building billing UI.

## Step 5 — Test before going live

`stripe listen --forward-to localhost:3000/api/webhook` and `stripe trigger checkout.session.completed`. Never ship without a real end-to-end webhook test.

## Pricing model defaults

- **3 tiers** (anchor / target / premium), middle one flagged "Most popular."
- Charge per **value metric** (seats, usage, projects), not per feature.
- Offer monthly + annual (annual ≈ 2 months free) to cut churn.
- Stripe is the **catalog source of truth** — set prices there, reference the IDs in code.

## Other providers (Mercado Pago and similar)

The flow is the same — create the charge server-side, fulfill on the webhook, stay idempotent — but verify these against a **real** payment, because sandboxes differ from production:

- **Which object carries which field.** A subscription event can arrive with the payer's email empty while the payment object has it. Treat empty as missing (`||`, not `??`) and fetch the object that holds the data.
- **Whether the sandbox is usable at all.** Some require both parties to be test accounts. A real plan at the minimum amount is a legitimate test.
- **The token's prefix.** Check that a key stored as "test" is a test key before it charges anyone.
- **The cancellation event may not identify the user.** Store the provider's customer and subscription ids against your user at sign-up.

## Subscription lifecycle (decide before launch)

- **Trial**: store an explicit `trial_ends_at`, set when the trial actually starts — not derived from `created_at`.
- **Failed renewal**: keep access while the provider is retrying; move to `past_due` only when it gives up.
- **Resubscribe**: cancel the previous subscription at the provider.
- **Provisioning is idempotent**: the second event for the same customer changes nothing — in particular, it does not issue new credentials.
- **Conversion tracking** fires once, when the account is created — not on every webhook.

## Field notes

`references/field-notes.md` holds 16 payment failures from production apps, each with symptom, cause and what fixed it. Read it before the first real charge. The three that cost the most:

1. The first paying customer got no account, because a field was empty in one object and present in another.
2. Checkout died with a "connection" error that was a trailing newline in the secret key.
3. Trial access was measured from sign-up instead of activation, locking out people who verified late.

## Output

Deliver: the integration choice, the `/api/checkout` and `/api/webhook` handlers with signature verification + idempotent fulfillment, the customer-portal redirect, the lifecycle-event handling, and the pricing tiers.

## Reference

stripe-samples (checkout-single-subscription, subscription-use-cases, accept-a-payment ~800-900⭐ each, active), Stripe Customer Portal + Build-subscriptions docs, Stripe MCP (`stripe/ai` ~1.6k⭐), InsForge Stripe integration (agentic-native, via `insforge` skills).
