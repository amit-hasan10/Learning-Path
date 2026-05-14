# Python Conditional Statements

This project demonstrates different types of conditional statements in Python such as:

- `if` statement
- `if-else` statement
- `elif` statement
- Nested `if` statement

These examples help beginners understand how decision-making works in Python programming.

---

# 1. Adult or Minor Check

```python
a = int(input("Enter a number: "))
print("Your number is: ", a)

if a > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

## Explanation

- The program takes a number as input from the user.
- If the number is greater than 18, it prints:

  ```
  You are an adult.
  ```

- Otherwise, it prints:

  ```
  You are a minor.
  ```

---

# 2. Comparing Two Numbers

```python
a = 20
b = 10

if a > b:
    print("a is greater than b.")
else:
    print("a is not greater than b.")
```

## Explanation

- Two variables `a` and `b` are assigned values.
- The program checks whether `a` is greater than `b`.
- Since `20 > 10`, the output will be:

```python
a is greater than b.
```

---

# 3. Using elif Statement

```python
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
elif num == 99:
    print("The number is special")
else:
    print("The number is negative.")

print("I am happy")
```

## Explanation

This program checks multiple conditions using `if`, `elif`, and `else`.

### Conditions

- If the number is greater than 0:

  ```
  The number is positive.
  ```

- If the number is equal to 0:

  ```
  The number is zero.
  ```

- If the number is equal to 99:

  ```
  The number is special
  ```

- Otherwise:

  ```
  The number is negative.
  ```

Finally, the program prints:

```python
I am happy
```

## Important Note

The condition:

```python
elif num == 99:
```

will never execute because `99` is already greater than `0`, so the first condition becomes true.

Correct order should be:

```python
if num == 99:
```

before checking `num > 0`.

---

# 4. Nested if Statement

```python
num1 = 17

if num1 < 0:
    print("The number is negative.")
elif num1 > 0:
    if num1 <= 10:
        print("The number is positive and less than or equal to 10.")
    elif num1 > 10 and num1 <= 20:
        print("The number is positive and between 11 and 20.")
    else:
        print("The number is positive and greater than 20.")
else:
    print("The number is zero.")
```

## Explanation

This example demonstrates a nested `if` statement.

### Working Process

1. First, the program checks whether the number is:
   - Negative
   - Positive
   - Zero

2. If the number is positive, another `if` statement checks:
   - Whether it is less than or equal to 10
   - Between 11 and 20
   - Greater than 20

For:

```python
num1 = 17
```

the output will be:

```python
The number is positive and between 11 and 20.
```

---

# Concepts Learned

After completing these examples, you will understand:

- How to use conditional statements in Python
- How decision-making works in programming
- Difference between `if`, `elif`, and `else`
- How nested conditions work
- How to compare values using relational operators

---

# How to Run the Program

1. Install Python on your computer
2. Save the code in a file named `main.py`
3. Open terminal or command prompt
4. Run the following command:

```bash
python main.py
```

---

# Conclusion

Conditional statements are very important in Python programming because they help programs make decisions based on different conditions. These examples provide a basic understanding of decision-making statements for beginners.