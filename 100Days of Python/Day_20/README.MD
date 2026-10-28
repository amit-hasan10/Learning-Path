# Python Lists

## Introduction
Lists are used to store multiple items in a single variable. They are one of the most commonly used data types in Python.

## 1. Creating a List
- Lists are created using square brackets `[]`.
- A list can contain different types of data.
- Lists are ordered and allow duplicate values.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

**Output:**
```text
['apple', 'banana', 'cherry']
```

## 2. Checking Items in a List
The `in` keyword is used to check whether an item exists in a list.

```python
marks = [90, 80, 70, 60, 50, "Amit"]

if 90 in marks:
    print("Yes, 90 is in the list of marks")
else:
    print("No, 90 is not in the list of marks")
```

We can also use `in` to check whether a character exists in a string.

```python
if "A" in "Amit":
    print("Yes, A is in Amit")
```

## 3. List Slicing
List slicing allows us to access a specific portion of a list.

**Syntax:**
```python
list_name[start:end:step]
```

- `start`: Starting index.
- `end`: Ending index (not included).
- `step`: Number of positions to skip.

Example:

```python
Marks = [90, 100, 30, 70, 80, 39, 33, 20, 50, 60, 70, 80, 90, 100]

print(Marks[1:8])
print(Marks[1:8:2])
```

**Output:**
```text
[100, 30, 70, 80, 39, 33, 20]
[100, 70, 39, 20]
```

## 4. List Comprehension
List comprehension provides a shorter and cleaner way to create a new list from an existing iterable, such as a list or range.

It can also include conditions to filter elements.

**Example 1: Creating a list using range()**

```python
lst = [x for x in range(10)]
print(lst)
```

**Output:**
```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Example 2: Creating a list of even numbers squared**

```python
lst1 = [x*x for x in range(10) if x % 2 == 0]
print(lst1)
```

**Output:**
```text
[0, 4, 16, 36, 64]
```

## Key Points to Remember

- Lists are created using square brackets `[]`.
- Lists can store multiple values in a single variable.
- Lists can contain different data types.
- List indexing starts from `0`.
- The `in` keyword checks whether an item exists.
- Slicing is used to access specific elements.
- List comprehension makes list creation easier and shorter.

## Conclusion
Python lists are useful for storing and managing multiple values. Understanding list creation, membership checking, slicing, and list comprehension will help build a strong foundation in Python programming.