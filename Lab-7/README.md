# Lab 7 - Fuzz Testing

Assigned repo: [SETAPESU26/L6_L7_43_warranty_claims](https://github.com/SETAPESU26/L6_L7_43_warranty_claims).
The Lab 7 script parses warranty claims, averages product ages and works out the payable repair charge. I fuzzed it with Hypothesis, found the inputs that crash it or give wrong results, and fixed it.

## Deliverables

| File | What it is |
|---|---|
| [PES1UG24CS171_Lab7_FuzzTesting_Report.pdf](PES1UG24CS171_Lab7_FuzzTesting_Report.pdf) | Report with screenshots for every step |
| [warranty_claims/warranty_claims.py](warranty_claims/warranty_claims.py) | Fixed application script |
| [warranty_claims/test_processor.py](warranty_claims/test_processor.py) | Hypothesis tests |

## Results

| Script | Passed | Failed |
|---|---|---|
| Original warranty_claims.py | 3 | 6 |
| Fixed warranty_claims.py | 9 | 0 |

Hypothesis found crashes on None, on a missing `:` or `|`, on empty numbers, and on empty items in the age list. It also showed that `nan` went through `parse_claim` and `payable_charge` without any error. The fixed version checks the input type, makes sure there are exactly two parts, and only accepts numbers that are finite and not negative. Anything else returns `None`, and `main()` prints a message saying what format it expected.

## Running it

```bash
cd warranty_claims
pip install hypothesis pytest
python warranty_claims.py
python -m pytest test_processor.py
```
