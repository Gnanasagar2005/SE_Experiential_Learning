# Lab 3 - Component Modelling & Architectural Pattern Selection

Problem Statement #43: **Feature Flag & Dynamic Config Manager**
(Developer Tools & IT Operations)

Evaluate the candidate architectural styles for the flag platform, select one, and model the
system as a UML component diagram with explicit provided and required interfaces.

## Contents

| File | What it is |
|---|---|
| [component-diagram.pdf](component-diagram.pdf) | UML component diagram - 7 components, 6 interfaces in ball-and-socket notation |
| [component-diagram.drawio](component-diagram.drawio) | Editable draw.io source for the diagram |
| [architecture-justification.pdf](architecture-justification.pdf) | Written justification: styles evaluated, selected style, mapping to the diagram, trade-off accepted |

## Architecture Selected

**Event-Driven Microservices.** Real-time flag sync to client SDKs is the defining requirement,
and a request/response style (layered or client-server) could only meet it by polling. Splitting
the system into services also lets the Rule Evaluation Engine, the busiest and most
latency-sensitive part (NFR-001: under 15 ms), scale on its own. The cost is more operational
work: several services and a message broker to run and monitor instead of one process.

| Style | Fit for real-time flag sync | Strength | Weakness |
|---|---|---|---|
| Layered | Poor: request/response only, no push to SDKs | Simple, well understood | Cannot support real-time client sync |
| Client-Server | Weak: clients must poll for updates | Easy to implement | Polling wastes bandwidth, delays rollout |
| Event-Driven Microservices | Strong: pub/sub pushes flag changes at once | Real-time sync, independent scaling | Higher operational complexity |

## Components

| Component | Responsibility |
|---|---|
| Admin Console | Release Manager UI for flags, cohorts and rollouts |
| Config Management API | Flag and cohort CRUD service |
| Rule Evaluation Engine | User ID hashing and cohort targeting (FR-001, NFR-001) |
| Config Store | Persistent database for flag and config data |
| Real-Time Sync Service | Pub/sub broker with WebSocket push to SDKs |
| Client SDK | Embedded in the consuming app; receives flag updates |
| Audit & Analytics Logger | Change history and usage metrics, kept off the request path |

## Interfaces

| Interface | Provided by | Required by | Style |
|---|---|---|---|
| IConfigManagement | Config Management API | Admin Console | direct |
| IConfigPersistence | Config Store | Config Management API, Rule Evaluation Engine | direct / indirect |
| IRuleEvaluation | Rule Evaluation Engine | Config Management API | synchronous |
| IRuleEvaluation (streamed) | Rule Evaluation Engine | Real-Time Sync Service | streamed |
| IFlagSync | Real-Time Sync Service | Client SDK | publish/subscribe |
| IAuditLog | Config Management API (change events) | Audit & Analytics Logger | event subscription |

The Audit & Analytics Logger subscribes to change events through `IAuditLog`, so audit logging
never adds latency to flag evaluation.
