# Day 16 – Python While Loops

## Introduction

A `while` loop in Python is used to execute a block of code repeatedly as long as a given condition is True.

Unlike a `for` loop, where we usually iterate through a sequence, a `while` loop continues running until its condition becomes False.

## 1. Basic While Loop

A `while` loop checks the condition before executing the code. If the condition is True, the loop runs. Once it becomes False, the loop stops.

```python
i = int(input("Enter a number: "))

while i < 10:
    print(i)
    i += 1

print("The while loop is over")
```

**Example output:**

```text
Enter a number: 5
5
6
7
8
9
The while loop is over
```

Here, the loop starts from the number entered by the user and continues until `i` becomes 10.

The `i += 1` statement increases the value of `i` by 1 after every iteration.

## 2. While Loop with Else

Python allows us to use an `else` block with a `while` loop.

The `else` block executes when the loop finishes normally because its condition becomes False.

```python
j = 0

while j <= 5:
    print(j)
    j += 1
else:
    print("The loop successfully completed")
```

**Output:**

```text
0
1
2
3
4
5
The loop successfully completed
```

In this example, the loop prints numbers from 0 to 5. When the condition becomes False, the `else` block executes.

## 3. While Loop with Break Statement

The `break` statement is used to stop a loop immediately, even if the loop condition is still True.

```python
i = 1

while i < 6:
    print(i)

    if i == 3:
        break

    i += 1
```

**Output:**

```text
1
2
3
```

Here, the loop stops when `i` reaches 3. The remaining iterations are skipped.

## 4. While Loop with Continue Statement

The `continue` statement skips the remaining statements in the current iteration and moves to the next iteration.

```python
i = 0

while i < 6:
    i += 1

    if i == 3:
        continue

    print(i)
```

**Output:**

```text
1
2
4
5
6
```

In this example, the number 3 is skipped because of the `continue` statement. The loop then continues with the next number.

Notice that `i += 1` is placed before `continue`. This is important to prevent an infinite loop.

## 5. Difference Between Break and Continue

| Break | Continue |
|---|---|
| Stops the entire loop. | Skips only the current iteration. |
| No further iterations execute. | The next iteration starts. |
| Used when we want to exit a loop. | Used when we want to skip a particular condition. |

## Key Takeaways

- `while`: Repeats a block of code while a condition is True.
- `i += 1`: Increases the variable by 1.
- `else`: Executes when the loop finishes normally.
- `break`: Immediately terminates the loop.
- `continue`: Skips the current iteration and continues with the next one.
- Always make sure your loop condition can eventually become False to avoid an infinite loop.

## Conclusion

Today I learned how to use Python while loops to execute code repeatedly based on a condition. I also learned how to control loop execution using `break` and `continue`, and how to use an `else` block with a while loop.

These concepts are useful for creating programs that need to repeat tasks, validate user input, and perform operations until a particular condition is met.