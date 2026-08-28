# Use-Case Flow: UC-02 Configure Percentage Rollout

Feature Flag & Dynamic Config Manager (Problem Statement #43)

Gnanasagar H, PES1UG24CS171, Section 5 - 'C'

Primary actor: Release Manager. Secondary actor: Client App SDK.
Related requirements: FR-001, FR-002, FR-004, FR-005, NFR-002.

## Preconditions

- The Release Manager has an account with permission to change flags in the target environment.
- The feature flag already exists (created through UC-01).
- At least one client SDK is connected to the target environment.

## Postconditions

- The flag's rollout percentage for that environment is saved as a new version.
- The change is written to the audit log with user, time, environment, old value and new value.
- All connected SDKs in that environment have the new rollout value within 5 seconds.

## Main Success Scenario

1. Release Manager logs in to the dashboard. The system authenticates them (includes Authenticate User).
2. Release Manager opens the flag "new-checkout-page" and picks the production environment.
3. The system shows the current rollout (for example 10%) and the targeting rules.
4. Release Manager enters a new rollout value of 25% and clicks Save.
5. The system checks that the value is a whole number from 0 to 100 and that the user may edit production.
6. The system saves the change as a new flag version and writes an audit log entry.
7. The system pushes the update to every SDK connected to production (includes Sync Flag Updates to SDKs).
8. Each SDK confirms it received the new value. From now on, users whose ID hash falls in the first 25 buckets get true.
9. The system shows "Rollout updated to 25%" with the number of SDKs that confirmed. The use case ends.

## Alternate Flows

### 5a. Invalid rollout value

- 5a1. The Release Manager enters a value outside 0 to 100, or a non-number such as 120 or "abc".
- 5a2. The system does not save anything and shows "Rollout must be a whole number between 0 and 100".
- 5a3. The Release Manager corrects the value and the flow continues from step 4.

### 8a. Some SDKs do not confirm within 5 seconds

- 8a1. The system marks those SDK clients as out of sync and retries the push up to 3 times.
- 8a2. If they still do not confirm, the dashboard shows a warning listing them. Those clients keep using their cached value (NFR-002) until they reconnect and pull the latest version.
- 8a3. The saved change is not undone. The Release Manager can choose Roll Back Flag Change (extends View Audit Log) if needed.
