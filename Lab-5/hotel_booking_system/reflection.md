# Reflection

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

The style ones were easy. The unused import, `== None`, the missing newline and the long line each took a few seconds, and Flake8 gives the exact column. Docstrings and renaming `bookRoom` were also quick, though for the rename I had to make sure the call in `main` changed too.

The eval one was the hardest. I couldn't just delete `eval` because the function still needs some way to take a pricing rule, so I had to work out what it was actually used for. Every call in the file only multiplied the base price, so I changed the parameter to a number. That changes the signature, and anything calling it with a string would break, which I decided was fine here. The secret key needed some thought for the same reason. Deleting it would have changed what the program does, so I moved it to an environment variable.

**2. Did the static analysis tools report any false positives? If so, describe one example.**

Bandit's B311 warning on `random.randint` is borderline. It says the generator isn't suitable for security, but a four digit booking number in a small demo isn't really a security value. I changed it to `secrets` anyway since it costs nothing and booking references often get used to look up reservations. B105 is also a guess, because Bandit only flagged that string due to the word "secret" in the variable name. In this case it happened to be right.

**3. How would you integrate static analysis tools into your actual software development workflow?**

I'd run Flake8 and Pylint in a pre-commit hook so style problems never get committed, and run all three in CI on every pull request. High and medium Bandit findings would fail the build, and so would a Pylint score below about 9.5. Running them locally first helps a lot, because fixing a warning right after writing the code is much quicker than coming back to it after review.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

The code no longer runs arbitrary strings with eval or hands filenames to a shell, and the secret isn't in the source or the output anymore. `cancel_booking` now tells the caller when the room doesn't exist instead of swallowing the error, and the booking log can't leak between calls through a shared default list. The ledger file gets closed even if the write fails. It's easier to read too: `check_room_status` is two lines now, each function has a docstring, and the module can be imported without running the demo. Pylint went from 5.32 to 10.00, and Bandit and Flake8 report nothing.

Some things the tools didn't catch. The demo calls `book_room` and `cancel_booking` and ignores what they return, so a failed booking would go unnoticed. Also, the repo README says the program asks the user a question, but this version of the script doesn't take any input.
