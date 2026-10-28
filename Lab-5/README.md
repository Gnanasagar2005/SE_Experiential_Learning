# Lab 5 - Static Code Analysis

Assigned repo: [SETAPESU26/L5_43_hotel_booking_system](https://github.com/SETAPESU26/L5_43_hotel_booking_system),
a hotel room booking script. It was checked with Pylint, Bandit and Flake8 and the reported issues were fixed.

## Contents

| File | What it is |
|---|---|
| [hotel_booking_system/hotel_booking_system.py](hotel_booking_system/hotel_booking_system.py) | The cleaned script |
| [hotel_booking_system/issues.md](hotel_booking_system/issues.md) | Issue table with type, lines, description and fix |
| [hotel_booking_system/reflection.md](hotel_booking_system/reflection.md) | Answers to the reflection questions |
| [hotel_booking_system/reports/before/](hotel_booking_system/reports/before/) | Pylint, Bandit and Flake8 reports on the original script |
| [hotel_booking_system/reports/after/](hotel_booking_system/reports/after/) | The same reports after the fixes |

## Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.32/10 | 10.00/10 |
| Bandit | 6 issues (2 high, 1 medium, 3 low) | No issues |
| Flake8 | 7 warnings | None |

The Bandit, Pylint and Flake8 fixes were made in three separate commits.

## Running it

```bash
cd hotel_booking_system
python hotel_booking_system.py
pip install pylint bandit flake8
pylint hotel_booking_system.py
bandit -r hotel_booking_system.py
flake8 hotel_booking_system.py
```
