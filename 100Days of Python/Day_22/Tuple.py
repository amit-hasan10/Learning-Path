'''
Tuple is a built-in data structure in Python that is used to store an ordered collection of items. Tuples are similar to lists, but they are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.
'''

tup = (1, 2, 3, 4, 5) #creating a tuple
print(tup) #prints the tuple
tup1 = (1,) # Without the comma, it will be considered as an integer and not a tuple
print(tup1) #prints the tuple with one element
if 2 in tup: #checking if an element is present in the tuple
    print("2 is present in the tuple") #prints if the element is present

tup2 = tup[1:4] #slicing the tuple
print(tup2) #prints the sliced tuple