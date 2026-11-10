'''
Tuples are immutable. Hence, if you want to add or remove elements from a tuple, you will have to convert it into a list first, perform the operation, and then convert it back to a tuple.
'''
country = ('USA', 'Canada', 'Germany', 'France', 'Italy')
temp = list(country)  # Convert tuple to list
temp.append('Spain')  # Add an element to the list
temp.pop(1)  # Remove an element from the list
temp[2] = 'Sweden'  # Modify an element in the list
country = tuple(temp)  # Convert list back to tuple
print(country)  # prints the modified tuple


countries1 = ('Bangladesh', 'India', 'Pakistan', 'Nepal', 'Bhutan')
countries2 = ('Sri Lanka', 'Maldives', 'Afghanistan', 'Myanmar', 'Thailand')
southeastasia = countries1 + countries2  # Concatenating two tuples
print(southeastasia)  # prints the concatenated tuple

tuple1 = (1, 2, 3, 4, 5,1, 2, 3, 4, 5)
res = tuple1.count(2)  # Counting the occurrences of an element in the tuple
print("Count of 2 in tuple1:", res)  # prints the count of 2 in tuple1

res1 = tuple1.index(3)  # Finding the first index of an element in the tuple
print("Index of 3 in tuple1:", res1)  # prints the index of 3 in tuple1
res2 = tuple1.index(1, 4)  # Finding the index of an element in the tuple starting from a specific index
print("Index of 1 in tuple1 starting from index 4:", res2)  # prints the index of 1 in tuple1 starting from index 4
res3 = tuple1.index(5, 5, 10)  # Finding the index of an element in the tuple within a specific range
print("Index of 5 in tuple1 between index 5 and 10:", res3)  # prints the index of 5 in tuple1 between index 5 and 10