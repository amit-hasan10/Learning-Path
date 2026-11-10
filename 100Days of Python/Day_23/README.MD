# Python Tuple Operations

A beginner-friendly Python project demonstrating tuple modification, concatenation, counting, and searching operations with practical code examples.

## About the Project

Tuples are built-in data structures in Python used to store ordered collections of items. They are **immutable**, meaning their elements cannot be directly modified after creation.

However, we can convert a tuple into a list, perform operations such as adding, removing, and modifying elements, and then convert it back into a tuple.

This project demonstrates different ways to work with and manipulate tuples in Python.

## Topics Covered

- Modifying tuples using list conversion.
- Adding elements to tuples.
- Removing elements from tuples.
- Updating tuple elements.
- Concatenating two tuples.
- Counting occurrences using `count()`.
- Finding element positions using `index()`.
- Searching within a specific index range.

## Code Examples

### 1. Modifying a Tuple

Since tuples are immutable, we first convert the tuple into a list to perform modifications.

```python
country = ('USA', 'Canada', 'Germany', 'France', 'Italy')

temp = list(country)
temp.append('Spain')
temp.pop(1)
temp[2] = 'Sweden'

country = tuple(temp)
print(country)
```

**Output:**
```text
('USA', 'Germany', 'Sweden', 'Italy', 'Spain')
```

### 2. Tuple Concatenation

The `+` operator is used to combine two or more tuples into a new tuple.

```python
countries1 = ('Bangladesh', 'India', 'Pakistan', 'Nepal', 'Bhutan')

countries2 = ('Sri Lanka', 'Maldives', 'Afghanistan', 'Myanmar', 'Thailand')

southeastasia = countries1 + countries2
print(southeastasia)
```

### 3. Count Method

The `count()` method returns the total number of occurrences of a specific element in a tuple.

```python
tuple1 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

res = tuple1.count(2)
print("Count of 2 in tuple1:", res)
```

**Output:**
```text
Count of 2 in tuple1: 2
```

### 4. Index Method

The `index()` method returns the index of the first occurrence of a specified element.

```python
res1 = tuple1.index(3)
print("Index of 3 in tuple1:", res1)
```

**Output:**
```text
Index of 3 in tuple1: 2
```

### 5. Finding an Element from a Specific Index

You can specify a starting index to search for an element.

```python
res2 = tuple1.index(1, 4)
print("Index of 1 in tuple1 starting from index 4:", res2)
```

**Output:**
```text
Index of 1 in tuple1 starting from index 4: 5
```

### 6. Finding an Element Within a Specific Range

The `index()` method also accepts a starting and ending index to search within a particular range.

```python
res3 = tuple1.index(5, 5, 10)
print("Index of 5 in tuple1 between index 5 and 10:", res3)
```

**Output:**
```text
Index of 5 in tuple1 between index 5 and 10: 9
```

## Important Tuple Methods

| Method / Operator | Description |
|---|---|
| `list()` | Converts a tuple into a list. |
| `tuple()` | Converts a list into a tuple. |
| `append()` | Adds an element to a list. |
| `pop()` | Removes an element from a list. |
| `+` | Concatenates two tuples. |
| `count()` | Counts occurrences of an element. |
| `index()` | Returns the index of an element. |

## Technologies Used

- Python 3
- Visual Studio Code
- Python IDLE

## How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Open the Python file.
4. Run the following command:

```bash
python main.py
```

## Learning Objectives

- Understand tuple immutability.
- Learn how to modify tuples through list conversion.
- Perform tuple concatenation.
- Understand the `count()` and `index()` methods.
- Search for elements within specific index ranges.
- Strengthen Python programming fundamentals.

## Author

**Md Amit Hasan Robi**