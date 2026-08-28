# Lab 1 - Requirements Engineering & UML Use-Case Modelling

Problem Statement #43: **Feature Flag & Dynamic Config Manager**
(Developer Tools & IT Operations)

A centralized configuration and feature toggling platform that supports percentage-based user
cohort rollouts, environment overrides, and real-time client SDK flag synchronization.

## Contents

| File | What it is |
|---|---|
| [requirements-table.md](requirements-table.md) | 5 functional + 2 non-functional requirements with priority, acceptance criteria and rationale, plus peer-critique notes |
| [use-case-diagram.pdf](use-case-diagram.pdf) | UML use-case diagram - 3 actors, 9 use cases, five «include» and one «extend» |
| [use-case-diagram.drawio](use-case-diagram.drawio) | Editable draw.io source for the diagram |
| [use-case-flow.md](use-case-flow.md) | Flow specification for UC-02 (Configure Percentage Rollout) with preconditions, postconditions, main success scenario and two alternate flows |

## Actors and Use Cases

**Actors:** Software Engineer, Release Manager, Client App SDK

| ID | Use Case |
|---|---|
| UC-01 | Create / Edit Feature Flag |
| UC-02 | Configure Percentage Rollout |
| UC-03 | Set Environment Override |
| UC-04 | Evaluate Feature Flag |
| UC-05 | View Audit Log |
| UC-06 | Sync Flag Updates to SDKs (included by UC-03 and UC-04) |
| - | Authenticate User (included by UC-01 and UC-02) |
| - | Apply Targeting Rules (included by UC-04) |
| - | Roll Back Flag Change (extends UC-05) |
