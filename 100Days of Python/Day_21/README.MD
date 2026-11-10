# Python List Methods

A simple Python project demonstrating essential built-in list methods and list operations with practical examples.

## About the Project

In Python, a list is a built-in data structure used to store multiple items in a single variable. Lists are ordered, mutable, and allow duplicate values.

This project covers commonly used list methods, including adding elements, sorting, searching, counting, copying, and combining lists.

## Topics Covered

| Method / Operation | Description |
|---|---|
| `append()` | Adds an element at the end of a list. |
| `sort()` | Sorts the list in ascending order. |
| `sort(reverse=True)` | Sorts the list in descending order. |
| `index()` | Returns the index of the first occurrence of an element. |
| `count()` | Returns the number of occurrences of an element. |
| `copy()` | Creates a shallow copy of a list. |
| `insert()` | Inserts an element at a specified position. |
| `extend()` | Adds elements from another list. |
| `+` Operator | Combines two lists through concatenation. |

## Code Examples

### 1. Append Method
```python
l = [1, 2, 3, 4, 5]
l.append(6)
print(l)
```
**Output:**
```text
[1, 2, 3, 4, 5, 6]
```

### 2. Sort Method
```python
l1 = [3, 8, 2, 9, 1, 99]

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)
```
**Output:**
```text
[1, 2, 3, 8, 9, 99]
[99, 9, 8, 3, 2, 1]
```

### 3. Index Method
```python
v = l1.index(9)
print(v)
```
Returns the position of the first occurrence of `9`.

### 4. Count Method
```python
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
print(l2.count(1))
```
**Output:**
```text
2
```

### 5. Reference vs Copy

**List Reference:**
```python
l = [1, 2, 3, 4, 5]
m = l
m[0] = 100
print(l)
```
Output: `[100, 2, 3, 4, 5]`

Both variables refer to the same list.

**List Copy:**
```python
l = [1, 2, 3, 4, 5]
m = l.copy()
m[0] = 100
print(l)
```
Output: `[1, 2, 3, 4, 5]`

The `copy()` method creates a separate shallow copy of the list.

### 6. Insert Method
```python
l = [1, 2, 3, 4, 5]
l.insert(2, 100)
print(l)
```
**Output:**
```text
[1, 2, 100, 3, 4, 5]
```

### 7. Extend Method
```python
l = [1, 2, 3, 4, 5]
m = [6, 7, 8]

l.extend(m)
print(l)
```
Adds all elements of `m` to `l`.

### 8. List Concatenation
```python
k = l + m
print(k)
```
Combines two lists into a new list.

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

- Understand Python list operations.
- Learn important built-in list methods.
- Understand list referencing and copying.
- Practice modifying and manipulating lists.
- Strengthen Python programming fundamentals.

## Author

**Md Amit Hasan Robi**
