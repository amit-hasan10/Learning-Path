# Python Lists

## Introduction
A list in Python is used to store multiple items in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.

## Creating a List

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)
```

## Accessing List Items

You can access list elements using their index. Indexing starts from 0.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])   # Apple
print(fruits[1])   # Banana
print(fruits[-1])  # Mango
```

## Changing List Items

Lists are mutable, which means we can change their values.

```python
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"

print(fruits)
```

## Adding Items to a List

- `append()` – Adds an item at the end.
- `insert()` – Adds an item at a specific position.
- `extend()` – Adds multiple items from another iterable.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")
fruits.insert(1, "Orange")
fruits.extend(["Grapes", "Pineapple"])

print(fruits)
```

## Removing Items from a List

- `remove()` – Removes a specific item.
- `pop()` – Removes an item by index.
- `del` – Deletes an item or the entire list.
- `clear()` – Removes all items.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")
fruits.pop(1)
fruits.clear()
```

## List Slicing

Slicing allows you to access a specific portion of a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

## Useful List Methods

| Method | Description |
|---|---|
| `append()` | Adds an item |
| `insert()` | Inserts an item |
| `extend()` | Adds multiple items |
| `remove()` | Removes a specific item |
| `pop()` | Removes an item by index |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `index()` | Returns the index of an item |
| `count()` | Counts occurrences |
| `copy()` | Creates a copy |
| `clear()` | Removes all items |

## Looping Through a List

You can use a `for` loop to access every