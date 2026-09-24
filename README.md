# Password Strength Checker

A Python script that evaluates the strength of a password against multiple security criteria and gives it a score out of 8, along with a strength level (Very Weak, Weak, Medium, Strong).

## What it checks

- Length (must be longer than 8 characters)
- Contains at least one English letter
- Contains at least one special character (`@`, `$`, `!`)
- Contains at least one uppercase letter
- Is not identical to the username
- Is not the swapcase version of the username (e.g. `john` → `JOHN`)
- Is not a "special-character" version of the username (e.g. `admin` → `@dm!n`, using common leetspeak substitutions)
- Is not one of the most common, easily-guessed passwords (e.g. `123456`, `password`, `qwerty`)

## Usage

```bash
python password_strength_checker.py
```

The script will prompt for a username and a password, then print:
- A detailed breakdown of which checks passed or failed
- A final score out of 8
- An overall security level with a tip for improvement

## Example

```
Please enter your username: john
Please enter your password: J0hn123!

Filter checks:
Password length is sufficient.
Contains at least one English letter.
Contains at least one special character.
...

Final Score: 6 out of 8
Security Level: Medium
Tip: Your password is fairly secure, but try to avoid using patterns based on your username.
```
