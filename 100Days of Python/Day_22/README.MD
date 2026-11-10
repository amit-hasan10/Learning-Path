# Python Tuples

A beginner-friendly Python project demonstrating tuple creation, properties, element checking, and slicing with simple code examples.

## About the Project

A **Tuple** is a built-in data structure in Python used to store an ordered collection of items.

Tuples are similar to lists, but the main difference is that tuples are **immutable**, meaning their elements cannot be changed, added, or removed after creation.

## Key Features of Tuples

- **Ordered:** Elements maintain their original order.
- **Immutable:** Elements cannot be modified after creation.
- **Allows Duplicates:** Multiple elements can have the same value.
- **Different Data Types:** Can store integers, strings, floats, and other objects.
- **Indexed:** Elements can be accessed using their index.

## Code Examples

### 1. Creating a Tuple

```python
tup = (1, 2, 3, 4, 5)
print(tup)
```

**Output:**
```text
(1, 2, 3, 4, 5)
```

### 2. Creating a Tuple with One Element

To create a single-element tuple, you must include a comma after the element.

```python
tup1 = (1,)
print(tup1)
```

**Output:**
```text
(1,)
```

**Note:** Without the comma, Python considers `(1)` an integer, not a tuple.

### 3. Checking Elements in a Tuple

The `in` operator checks whether a particular element exists in a tuple.

```python
if 2 in tup:
    print("2 is present in the tuple")
```

**Output:**
```text
2 is present in the tuple
```

### 4. Tuple Slicing

Slicing allows you to access a specific portion of a tuple.

```python
tup2 = tup[1:4]
print(tup2)
```

**Output:**
```text
(2, 3, 4)
```

**Explanation:**
- Starting index: `1` (included)
- Ending index: `4` (excluded)

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

- Understand Python tuples and their properties.
- Learn how to create single-element and multiple-element tuples.
- Understand tuple immutability.
- Check elements using the `in` operator.
- Perform tuple slicing.
- Understand the differences between lists and tuples.

## Author

**Md Amit Hasan Robi**