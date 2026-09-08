# Lab 2 - Agile Backlog Creation & Sprint Simulation in Jira

Problem Statement #43: **Feature Flag & Dynamic Config Manager**
(Developer Tools & IT Operations)

Turn the Lab 1 functional requirements into Jira epics and user stories, prioritise and
estimate them with story points, then run two sprints on a Scrum board and read the burndown.

## Contents

| File | What it is |
|---|---|
| [epics-and-user-stories.pdf](epics-and-user-stories.pdf) | The 5 epics and 17 user stories with priority, story points and sprint |
| [reflection.pdf](reflection.pdf) | Answers to the four reflection questions, with the burndown charts |
| [screenshots/](screenshots/) | Jira backlog, active sprint boards, epic progress and burndown charts |

## Epics

| Key | Epic | From Lab 1 | Priority | Points |
|---|---|---|---|---|
| SCRUM-5 | Flag Evaluation & User Targeting | FR-001, NFR-001 | High | 16 |
| SCRUM-6 | Percentage Rollout Management | FR-002 | High | 9 |
| SCRUM-7 | Environment Overrides | FR-003 | High | 10 |
| SCRUM-8 | Real-Time SDK Flag Sync | FR-004, NFR-002 | Medium | 19 |
| SCRUM-9 | Audit Log & Rollback | FR-005 | Medium | 10 |

Three setup tasks (repository and CI, data schema, environments) add 7 more points, for a
backlog of 71 points.

## Sprints

| Sprint | Goal | Planned | Completed |
|---|---|---|---|
| Sprint 1 - Core Flag Engine | Flag evaluation with hash bucketing, percentage rollouts and per-environment values | 35 | 30 |
| Sprint 2 - Sync & Audit | Real-time push to SDKs, offline fallback, audit log with rollback | 41 | 39 |

SCRUM-16 (the 10,000-user distribution test) did not finish in Sprint 1 and was carried into
Sprint 2. SCRUM-19 (side-by-side environment view, Low priority) was dropped back to the
backlog at the end of Sprint 2.

## Screenshots

| File | Shows |
|---|---|
| 01-backlog-epics-and-story-points.png | Backlog with both sprints, epic tags and story points |
| 02-active-sprint-board-day1.png | Sprint 1 board early in the sprint |
| 03-active-sprint-board-day2.png | Sprint 1 board later in the sprint |
| 04-burndown-sprint1.png | Sprint 1 burndown chart |
| 05-active-sprint2-board.png | Sprint 2 board |
| 06-epic-progress-overview.png | Progress of all five epics |
| 07-burndown-sprint2.png | Sprint 2 burndown chart |
