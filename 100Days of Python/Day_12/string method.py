# Strings are immutable in Python
a = "Amit"
print(len(a))
print(a.upper())# converts to uppercase
print(a.lower())# converts to lowercase
b = "!!! Amitt !!!!!"
print(len(b))
print(b.rstrip("!"))# removes the trailing characters
print(b.lstrip("!"))# removes the leading characters
print(a.replace("Amit", "Amit Kumar"))# replaces a substring with another substring
c = "Amit Hasan Robi"
print(c.split(" "))# splits the string into a list based on the delimiter
blogHeading = "introduction-to-python-programming"
print(blogHeading.capitalize())# capitalizes the first character of the string
str1 = "Hello"
print(len(str1))
print(str1.center(50)) # centers the string within a specified width
str2 = "Hello World"
print(str2. endswith("World")) # checks if the string ends with the specified suffix
"abc123".isalnum()   # True
"abc".isalpha()     # True
"123".isdigit()     # True
"   ".isspace()     # True
"Title Case".istitle()  # True
print("Hello\tWorld") # \t is used to add a tab space between two words
print("Hello\nWorld") # \n is used to add a new line between two words
print("Hello\\World") # \\ is used to add a backslash between two words