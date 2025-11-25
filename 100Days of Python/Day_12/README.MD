🧵 Python String Methods

A complete guide with explanations and examples

Python provides many built-in string methods for text manipulation. This document gives clear explanations, categorized lists, and examples — perfect for beginners and useful for revision.

📚 Table of Contents

Changing Case

Searching in Strings

Replacing Text

Splitting & Joining

Removing Whitespace

String Check Methods

Formatting Methods

Other Useful Methods

Example Program

Summary Table

🔤 Changing Case
lower()

Converts all characters to lowercase.

"Hello World".lower()   # 'hello world'

upper()

Converts all characters to uppercase.

"Hello World".upper()   # 'HELLO WORLD'

title()

Capitalizes first letter of each word.

"python programming".title()   # 'Python Programming'

capitalize()

Capitalizes only the first character.

"python".capitalize()   # 'Python'

🔍 Searching in Strings
find(substring)

Returns index of first occurrence (-1 if not found):

"python".find("th")   # 2

rfind(substring)

Searches from the right:

"banana".rfind("a")   # 5

index() / rindex()

Like find() but throws error if not found:

"hello".index("e")   # 1

🔄 Replacing Text
replace(old, new)
"Java is fun".replace("Java", "Python")
# 'Python is fun'

✂️ Splitting & Joining
split(separator)
"a,b,c".split(",")   # ['a', 'b', 'c']

join(iterable)
"-".join(["2025", "01", "01"])
# '2025-01-01'

🧹 Removing Whitespace
strip()

Removes whitespace from both ends.

"  hello  ".strip()   # 'hello'

lstrip()
"   hi".lstrip()   # 'hi'

rstrip()
"bye   ".rstrip()   # 'bye'

🔢 String Check Methods

Return True/False.

isdigit()
"123".isdigit()   # True

isalpha()
"abc".isalpha()   # True

isalnum()
"abc123".isalnum()   # True

islower() / isupper()
"hello".islower()   # True

isspace()
"   ".isspace()   # True

🎨 Formatting Methods
center(width)
"hi".center(10)
# '    hi    '

ljust(width, fillchar)
"Amit".ljust(10, "-")
# 'Amit------'

rjust(width, fillchar)
"Amit".rjust(10, ".")
# '......Amit'

🧩 Other Useful Methods
startswith(prefix)
"hello.py".startswith("hello")   # True

endswith(suffix)
"hello.py".endswith(".py")   # True

count(substring)
"banana".count("a")   # 3

🧪 Example Program
text = " Python Programming "

print(text.strip().upper())
print(text.strip().replace("Python", "Java"))
print(text.lower().count("p"))
print("-".join(text.strip().split()))
