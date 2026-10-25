# Day 17 – Python Break and Continue Statements

## Introduction

In Python, `break` and `continue` are two important loop control statements.

Both are used to control how a loop works, but they have different purposes.

- `break` immediately stops the loop.
- `continue` skips the current iteration and moves to the next one.

Let's understand them with examples.

## 1. Break Statement

The `break` statement is used to terminate a `for` or `while` loop immediately, even if the loop condition is still True or there are more items remaining.

### Example: Multiplication Table Using Break

```python
for i in range(12):
    print("5 X", i, "=", 5 * i)

    if i == 10:
        break

print("The loop is broken")
```

**Output:**

```text
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
The loop is broken
```

**Explanation:**

- The loop starts from 0 and goes up to 11.
- It prints the multiplication table of 5.
- When `i` becomes 10, the `break` statement executes.
- The loop stops immediately, so 5 X 11 is never printed.
- Finally, the program prints "The loop is broken".

## 2. Continue Statement

The `continue` statement skips the remaining code in the current iteration and moves directly to the next iteration.

Unlike `break`, it does not terminate the entire loop.

### Example: Skipping an Iteration

```python
for i in range(12):
    if i == 10:
        print("Skipping the iteration when i is 10")
        continue

    print("5 X", i, "=", 5 * i)
```

**Output:**

```text
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
Skipping the iteration when i is 10
5 X 11 = 55
```

**Explanation:**

- The loop starts from 0 and continues up to 11.
- When `i` becomes 10, the condition becomes True.
- The message "Skipping the iteration when i is 10" is printed.
- The `continue` statement skips the multiplication statement for that iteration.
- The loop continues with the next value, which is 11.

## 3. Difference Between Break and Continue

| Break | Continue |
|---|---|
| Terminates the entire loop. | Skips only the current iteration. |
| No further iterations are executed. | The next iteration continues normally. |
| Used to exit a loop early. | Used to skip specific iterations. |

## Key Takeaways

- `break` completely stops a loop.
- `continue` skips the current iteration.
- Both statements work with `for` and `while` loops.
- `break` is useful when a particular condition requires us to exit.
- `continue` is useful when we want to ignore certain values without stopping the loop.

## Conclusion

Today I learned how to control loops using Python's `break` and `continue` statements. I practiced printing a multiplication table and understood how to stop a loop completely or skip a particular iteration.

These statements make loops more flexible and help us control program execution based on specific conditions.