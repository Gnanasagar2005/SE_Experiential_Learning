# Issues found in hotel_booking_system.py

Line numbers are from the original file as given in the assignment repo. The full tool output is in reports/before and reports/after.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command built from input (Bandit B605) | Security, High | 58 | `os.system("echo ... " + filename)` passes the filename to a shell, so a filename like `x; del *` would run as a command | Removed the shell call and used `print()` for the message |
| Weak MD5 hash (Bandit B324) | Security, High | 47 | Guest ids were hashed with MD5, which is broken and easy to brute force | Switched to `hashlib.sha256` |
| Use of eval (Bandit B307, Pylint W0123) | Security, Medium | 40-43 | `compute_seasonal_rate` ran `eval()` on a string, so any Python code passed in would execute | The function now takes a numeric multiplier and returns `price * float(multiplier)` |
| Hardcoded secret (Bandit B105) | Security, Low | 62, 71 | The admin token was written in the source and printed to the console on every run | Read it from the `HOTEL_SECRET_KEY` environment variable and only print whether it is set |
| Insecure random for booking refs (Bandit B311) | Security, Low | 51 | `random.randint` is predictable, so references could be guessed | Used `secrets.randbelow(9000) + 1000`, same range as before |
| try/except/pass with bare except (Bandit B110, Pylint W0702, Flake8 E722) | Bug | 24-27 | Cancelling a room that does not exist failed silently and the caller had no way to know | Catch only `KeyError` and return False, return True on success |
| Mutable default argument (Pylint W0102) | Bug | 15 | `booking_log=[]` is created once and shared by every call that leaves it out, so log entries pile up across bookings | Default is `None` and a new list is created inside the function |
| Unused variables (Pylint W0612, Flake8 F841) | Code quality | 31, 41 | `cleaning_deposit` was never used, and `base_price` only existed so `eval` could see it | Removed `cleaning_deposit`, used the price directly |
| Comparison to None (Pylint C0121, Flake8 E711) | Style | 32 | `== None` instead of `is None` | Changed to `is None` |
| Redundant if/else returning booleans (Pylint R1703, R1705) | Code quality | 34-37 | An if/else that only returns True or False | `return not room_inventory[room_num]["is_booked"]` |
| File opened without `with` or encoding (Pylint R1732, W1514) | Bug | 55-57 | The file is not closed if `write` raises, and the encoding depends on the OS | `with open(filename, "w", encoding="utf-8")` |
| Function name not snake_case (Pylint C0103) | Style | 15 | `bookRoom` | Renamed to `book_room` and updated the call in `main` |
| Missing docstrings (Pylint C0116) | Style | 15, 23, 30, 40, 46, 50, 54, 61 | No function docstrings | Added a one line docstring to each function |
| Old style % formatting (Pylint C0209) | Style | 19 | `"..." % (a, b)` | Used an f-string |
| Unused import (Pylint W0611, Flake8 F401) | Style | 6 | `math` was imported and never used | Removed the import |
| Line too long (Flake8 E501) | Style | 19 | 80 characters, limit is 79 | Fixed when the line was rewritten as an f-string |
| No newline at end of file (Pylint C0304, Flake8 W292) | Style | 73 | Last line had no newline | Added it |
| main() runs on import | Code quality | 73 | Importing the module ran the whole demo and wrote a file. No tool flagged this | Wrapped the call in `if __name__ == "__main__":` |

After the fixes Pylint went from 5.32/10 to 10.00/10, Bandit went from 6 issues (2 high, 1 medium, 3 low) to none, and Flake8 went from 7 warnings to none. The program prints the same values as before apart from the hash (now SHA-256), the random booking reference, and the secret key, which is no longer shown.
