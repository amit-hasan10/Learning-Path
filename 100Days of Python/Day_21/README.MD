# Python List Methods

## Introduction

Python provides several built-in methods to perform different operations on lists. These methods help us add, remove, sort, and search for elements easily.

## 1. append()

The `append()` method is used to add a new element at the end of a list.

**Example:**

```python
l = [1, 2, 3, 4, 5]
l.append(6)
print(l)
```

**Output:**
```text
[1, 2, 3, 4, 5, 6]
```

## 2. sort()

The `sort()` method is used to arrange the elements of a list in ascending order by default.

**Example:**

```python
l1 = [3, 8, 2, 9, 1, 99]
l1.sort()
print(l1)
```

**Output:**
```text
[1, 2, 3, 8, 9, 99]
```

## 3. sort(reverse=True)

The `sort(reverse=True)` method arranges the elements of a list in descending order.

**Example:**

```python
l1 = [3, 8, 2, 9, 1, 99]
l1.sort(reverse=True)
print(l1)
```

**Output:**
```text
[99, 9, 8, 3, 2, 1]
```

## 4. index()

The `index()` method returns the index (position) of the first occurrence of a specified element in a list.

Remember that Python indexing starts from `0`.

**Example:**

```python
l1 = [3, 8, 2, 9, 1, 99]

print(l1.index(9))
```

**Output:**
```text
3
```

Here, the element `9` is located at index `3`.

## Key Points to Remember

- `append()`: Adds an element at the end of a list.
- `sort()`: Sorts elements in ascending order.
- `sort(reverse=True)`: Sorts elements in descending order.
- `index()`: Returns the index of the first occurrence of an element.
- These methods modify the original list, except that `index()` only searches for an element and returns its position.

## Conclusion

Python list methods make it easier to manage and organize list elements. Understanding these methods is important for writing efficient Python programs.