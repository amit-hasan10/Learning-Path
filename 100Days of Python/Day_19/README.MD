# Python Functions – Arguments and Parameters

## Introduction
In Python, functions can receive information from outside through **arguments**. These arguments allow us to pass different values to a function whenever we call it.

## 1. Passing Arguments to a Function

Arguments are written inside the parentheses when calling a function. We can pass multiple arguments by separating them with commas.

### Example 1: Single Argument

```python
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

**Output:**
```text
Emil Refsnes
Tobias Refsnes
Linus Refsnes
```

Here, the function receives a name and adds `" Refsnes"` to it.

## 2. Parameters and Arguments

Parameters and arguments are related, but they are not exactly the same.

- **Parameter:** The variable written inside the function definition.
- **Argument:** The actual value passed when calling the function.

### Example 2:

```python
def my_function(name):  # name is a parameter
    print("Hello", name)

my_function("Emil")  # "Emil" is an argument
```

**Output:**
```text
Hello Emil
```

In this example:
- `name` is the parameter.
- `"Emil"` is the argument.

## 3. Number of Arguments

By default, a function must receive the correct number of arguments when it is called.

For example, if a function expects two arguments, we must provide exactly two arguments.

### Example 3: Two Arguments

```python
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

**Output:**
```text
Emil Refsnes
```

Here, `fname` and `lname` are two parameters, while `"Emil"` and `"Refsnes"` are the arguments.

If we provide fewer or more arguments than required, Python raises a `TypeError`.

## Key Points to Remember

1. Arguments allow us to pass information to functions.
2. Parameters are variables defined in a function.
3. Arguments are actual values passed during a function call.
4. Multiple arguments must be separated by commas.
5. By default, the number of arguments must match the number of required parameters.

## Conclusion

Functions become more useful when we can pass different values to them. By understanding parameters and arguments, we can write reusable code and avoid unnecessary repetition.