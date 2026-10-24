# Python Match-Case Statement

This is a simple Python program that demonstrates how to use the `match-case` statement to check a user's input and display different messages based on the entered number.

I created this program to understand how pattern matching works in Python and how conditions can be used with a `match-case` statement.

# What This Program Does

- Takes an integer as input from the user.
- Checks whether the number is `1`, `2`, or `4`.
- Prints a specific message if one of these numbers is entered.
- Uses conditional guards to check other values.

# Code

x = int(input("Enter a number: "))

match x:
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 4:
        print("X is 4")
    case _ if x != 90:
        print(x, "is not equal to 90")
    case _ if x != 80:
        print(x, "is not equal to 80")
```


# How to Run
. Enter a number when prompted and check the output.

# Example Output

*Input:

Enter a number: 1
**Output:**

X is 1


Another example:

**Input:**

Enter a number: 50


**Output:**

50 is not equal to 90


## What I Learned

Through this program, I practised using Python's `match-case` statement, the wildcard pattern (`_`), and conditional guards with `if`.

# # Note

The two guarded cases at the end behave differently than they might first appear. For any number other than `1`, `2`, or `4`, the condition `x != 90` matches first unless `x` is `90`. Therefore, the final case checking `x != 80` is reached only when `x` is `90`, and its condition is also false. As a result, entering `90` produces no output.

This is a useful example of why the order of cases and the conditions used in pattern matching matter.
