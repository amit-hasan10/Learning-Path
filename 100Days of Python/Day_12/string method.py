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
print(len(str1.center(50))) # the length of the centered string will be equal to the specified width
str2 = "Hello World"
print(str2.endswith("World")) # checks if the string ends with the specified suffix
str4 = "He's an amazing person. He is always willing to help others."
print(str4.find("is")) # returns the index of the first occurrence of the specified substring
str5 = "HelloWorld"
print(str5.isalnum()) # checks if all characters in the string are alphanumeric
print(str5.isalpha()) # checks if all characters in the string are alphabetic

str6= "Hey What Are You Doing?"
print(str6.istitle()) # checks if the string is in title case