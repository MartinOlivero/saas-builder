# Multi-tenancy — field notes

From a B2B CRM that went from "one user, one organization" to memberships in production, a multi-dealership lead system, and a B2B ordering portal.

Format: **Symptom** → **Cause** → **What held**.

## The migration to memberships

**1. 39 of 56 policies, 21 functions and 33 files filtered by the user's organization.**
- What made it survivable: almost all of them already went through one function. Keeping that function and making it return the *active* workspace avoided rewriting the permissions.

**2. A person with two companies disappeared from the one they did not have open.**
- Cause: the team was listed by reading each user's current organization.
- Symptom in three places: the users screen, the public booking link, and lead distribution.
- What held: a `team` view built from memberships; 25 reads changed.

**3. Deleting an organization deleted the person.**
- Cause: `ON DELETE CASCADE` from organization to profile, harmless while every person had exactly one.

**4. "Delete user" deleted the account of someone who still belonged elsewhere.**

**5. The admin of company A changed the name and working hours of someone shared with B.**

**6. A personal integration stored company B's data inside company A.**

**7. A person with two memberships was invisible for a few minutes during the rollout.**
- Cause: order of release. The correct order turned out to be frontend → restricting migration → invitation functions.
- What held: the migration split in two parts (one that only adds, one that restricts and ships after the code), rehearsed inside `BEGIN … ROLLBACK`, with a written rollback. The rehearsal caught a defect in the plan before it reached production.

## Code that skips the policies

**8. A server function took the organization id from the request body and queried with the admin key.**

**9. A booking function counted an advisor's appointments without filtering by tenant.**
- Effect: for someone with membership in two tenants, workload from one skewed assignment in the other.
- It ran as `SECURITY DEFINER`, called with the admin client — no policy ever saw it.

**10. Fourteen functions checked organization but not "active user" or "valid subscription".**
- The screens checked all three. A deactivated user could still call the server directly.
- What held: one SQL gate, and a test comparing the server's answer with the screen's for every role combination.

**11. A role check returned the first membership row it could see.**
- Any reader passed as admin; the audit log recorded the action under another person's name.

**12. A reminder job with the admin key could have messaged another agency's customer.**
- Noted as open debt: one foreign key did not carry the tenant. Composite keys close it.

## The front door

**13. Three strangers created organizations in one day.**
- The registration page was already closed. Social login still reached the onboarding step that created the organization, by calling its function.
- What held: revoking execute on that function. A notification on new organizations was added — nobody had been told.

**14. Removing access left the password working.**
- Cause: the membership row was deleted, the auth user was not. Re-inviting failed with "email already exists".

**15. An invited person never managed to accept.**
- Cause: they opened the link while signed in as someone else and were bounced to the dashboard.
- Separately, the accept function discarded a read error and treated it as "no organization", moving a person out of their other company.

## The demo

**16. Visitors to the shared demo were admins.**
- They could spend the AI key by running audits, change or disconnect that key, and insert or delete reports. The demo password was in the JavaScript bundle.
- What held: a refusal for the demo organization in each server function, policies that exclude it, failing closed when the code cannot tell, and access through a personal link valid for 48 hours.
- Still open at the time of writing: one settings table remained writable in the demo through the API. Hiding the screen had not closed it.

**17. The demo dashboard showed zero.**
- Cause: a job moved the seeded dates forward but not the derived "month" column the dashboard filtered by.

## Tenant settings

**18. Slots were offered from 5 to 14 local time.**
- Cause: users with no time zone set defaulted to UTC.

**19. The customer and the advisor saw different times for the same appointment.**
- Cause: slot calculation in SQL used GMT; the panel formatted with the server process's zone.
- In another app the time zone column existed and nothing ever wrote to it.

**20. A customer saw a debt of 75.7 M instead of 3.9 M.**
- Cause: the balance view ran as the caller, who could read their sales but not their payments. Totals computed under row filtering depend on who is looking.
