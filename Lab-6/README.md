# Lab 6 - Code and Branch Coverage

Assigned repo: [SETAPESU26/L6_L7_43_warranty_claims](https://github.com/SETAPESU26/L6_L7_43_warranty_claims).
It's a small module that works out repair charges after a warranty runs out, decides whether a claim can be filed, and reports how close a claim is to its service deadline. Tests were added until line coverage and then branch coverage passed 90%.

## Contents

| File | What it is |
|---|---|
| [warranty_claims/warranty_claims.py](warranty_claims/warranty_claims.py) | Module under test, unchanged from the assignment repo |
| [warranty_claims/test_warranty_claims.py](warranty_claims/test_warranty_claims.py) | Starter tests from the assignment repo |
| [warranty_claims/CodeCoverageTest_warranty_claims.py](warranty_claims/CodeCoverageTest_warranty_claims.py) | Tests written for line coverage |
| [warranty_claims/BranchCoverageTest_warranty_claims.py](warranty_claims/BranchCoverageTest_warranty_claims.py) | Tests written for branch coverage |
| [warranty_claims/screenshots/code-coverage.png](warranty_claims/screenshots/code-coverage.png) | Terminal output for the line coverage run |
| [warranty_claims/screenshots/branch-coverage.png](warranty_claims/screenshots/branch-coverage.png) | Terminal output for the branch coverage run |

## Results

Coverage is measured on `warranty_claims.py` only.

| Test file | Tests | Line coverage | Branch coverage |
|---|---|---|---|
| test_warranty_claims.py (starter) | 2 | 38% | 32% |
| CodeCoverageTest_warranty_claims.py | 11 | 97% | 95% |
| BranchCoverageTest_warranty_claims.py | 24 | 100% | 100% (26/26 branches) |

The starter tests only reached the within-warranty case and one allowed claim, so most of the charge logic and all of `sla_status` never ran.

The line coverage tests run every statement except line 18 (`rate = 100`), which only runs for a defect claim past warranty. None of these tests use one. Branch coverage comes out at 95% since only two branches were never taken: the `else` that leads to line 18, and the jump from line 21 to the return when a claim more than 12 months over isn't accidental.

The branch tests send every condition both ways and check the boundary values too: an age of 0, an excess of exactly 0 and exactly 12, 29 and 30 days since the last claim, 5 and 6 recall claims, and hours left sitting right on each SLA cutoff. They also check that registration adds 6 months to basic and standard plans but not to premium. Line coverage can't show the premium case, because line 11 already runs for a registered standard plan.

## Running it

```bash
cd warranty_claims
pip install coverage pytest

coverage run -m pytest CodeCoverageTest_warranty_claims.py
coverage report -m --include=warranty_claims.py

coverage run --branch -m pytest BranchCoverageTest_warranty_claims.py
coverage report -m --include=warranty_claims.py
```
