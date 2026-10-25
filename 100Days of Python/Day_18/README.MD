# Day 18 – Python Functions

## Introduction

A function in Python is a block of reusable code that performs a specific task. Instead of writing the same code again and again, we can create a function and call it whenever we need it.

Functions help us keep our code organized, readable, and reusable.

### Why do we use functions?

- To avoid repeating the same code.
- To make programs easier to understand.
- To divide a large program into smaller parts.
- To perform specific tasks whenever needed.
- To return results from calculations.

## 1. Creating and Calling a Function

We use the `def` keyword to create a function. To execute the function, we need to call it using its name.

### Example: Calculate the Mean of Two Numbers

```python
def calculate_mean(a, b):
    mean = (a + b) / 2
    print(mean)

a = 7
b = 9

calculate_mean(a, b)
```

**Output:**

```text
8.0
```

**Explanation:**

- `def` is used to define a function.
- `calculate_mean` is the function name.
- `a` and `b` are parameters that receive values.
- The function calculates the average of two numbers.
- `calculate_mean(a, b)` calls the function and passes the values 7 and 9.

The formula used is:

Mean = (a + b) / 2

## 2. Function with If-Else Condition

We can also use conditional statements inside a function to perform different operations depending on the given values.

### Example: Find the Greater Number

```python
def isgreater(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")

c = 10
d = 5

isgreater(c, d)
```

**Output:**

```text
a is greater than b
```

**Explanation:**

- The function takes two