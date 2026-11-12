# Day 24 – Time-Based Greeting Program

## Description
A simple Python program that takes an hour from the user and displays a greeting based on the entered time.

## Concepts Covered
- Python `time` module
- `time.strftime()` function
- User input using `input()`
- Type conversion using `int()`
- Conditional statements (`if`, `elif`)
- Logical operators (`and`)

## How It Works
1. Imports the `time` module.
2. Gets the current time and hour.
3. Takes an hour (0–23) from the user.
4. Uses conditional statements to display the appropriate greeting.

## Greeting Conditions

| Hour | Greeting |
|---|---|
| 0–11 | Good Morning |
| 12–17 | Good Afternoon |
| 18–23 | Good Evening |

## Example Output
```text
Enter hour: 14
14
Good Afternoon
```

## How to Run
```bash
python Practice.py
```

## Author
Md Amit Hasan Robi