# Day 15 – Python For Loops

## Introduction

A `for` loop in Python is used to iterate over a sequence of items. These sequences can be lists, tuples, dictionaries, sets, or strings.

It allows us to execute a block of code once for each item in a sequence without writing the same code repeatedly.

## 1. Basic For Loop

We can use a `for` loop to access each item in a list one by one.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
```

**Output:**
```text
apple
banana
cherry
```

## 2. Looping Through a String

A `for` loop can also iterate through each character of a string.

```python
for x in "banana":
    print(x)
```

**Output:**
```text
b
a
n
a
n
a
```

## 3. The Break Statement

The `break` statement is used to stop a loop before it finishes all its iterations.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break
```

**Output:**
```text
apple
banana
```

In this example, the loop stops as soon as it reaches banana.

### Break Before Print

We can also place the `break` statement before the `print()` statement.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)
```

**Output:**
```text
apple
```

Here, banana is not printed because the loop stops before executing the print statement.

## 4. The Continue Statement

The `continue` statement skips the current iteration and moves to the next item in the loop.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)
```

**Output:**
```text
apple
cherry
```

In this example, banana is skipped, but the loop continues with cherry.

## 5. The Range() Function

The `range()` function is used when we want to execute a loop a specific number of times.

By default, it starts from 0, increases by 1, and stops before reaching the specified number.

```python
for x in range(6):
    print(x)
```

**Output:**
```text
0
1
2
3
4
5
```

### Specifying the Starting Value

We can specify both the starting and ending values using `range(start, stop)`.

```python
for x in range(2, 6):
    print(x)
```

**Output:**
```text
2
3
4
5
```

Remember that the ending number is not included.

### Specifying the Increment Value

We can also specify how much the value should increase in each iteration.

```python
for x in range(2, 30, 3):
    print(x)
```

**Output:**
```text
2
5
8
11
14
17
20
23
26
29
```

Here, the loop starts from 2 and increases by 3 each time.

## 6. The Else Statement in a For Loop

Python allows us to use an `else` block with a `for` loop.

The `else` block executes when the loop finishes normally.

```python
for x in range(6):
    print(x)
else:
    print("Finally finished!")
```

**Output:**
```text
0
1
2
3
4
5
Finally finished!
```

### Else With Break

If a loop is stopped using the `break` statement, the `else` block will not execute.

```python
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
```

**Output:**
```text
0
1
2
```

The `else` block is skipped because the loop was terminated by `break`.

## 7. Nested For Loops

A nested loop means placing one loop inside another loop.

The inner loop executes completely for every single iteration of the outer loop.

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```

**Output:**
```text
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
```

In this example, each adjective is combined with every fruit.

## Key Takeaways

- `for` loop: Used to iterate through a sequence.
- `break`: Stops the loop completely.
- `continue`: Skips the current iteration.
- `range()`: Generates a sequence of numbers.
- `else`: Executes when the loop finishes normally without a `break`.
- Nested loop: A loop inside another loop.

## Conclusion

Today I learned how to use Python `for` loops to work with different sequences, repeat tasks, control loop execution using `break` and `continue`, generate number sequences with `range()`, and work with nested loops.

These concepts are important because loops help us write shorter, cleaner, and more efficient Python programs.