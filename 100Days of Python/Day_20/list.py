#Lists are used to store multiple items in a single variable
#Lists are created using square brackets
thislist = ["apple", "banana", "cherry"]
print(thislist)

marks = [90, 80, 70, 60, 50,"Amit"]
if 90 in marks:
    print("Yes, 90 is in the list of marks")
else:
    print("No, 90 is not in the list of marks")
if "A" in "Amit":
    print("Yes, A is in Amit")

Marks = [90,100,30,70,80,39,33,20,50,60,70,80,90,100]
print(Marks[1:8])
print(Marks[1:8:2]) #jumps 2 index after every iteration

#List comprehension is a concise way to create lists from another list or iterable object. It consists of an expression followed by a for loop inside square brackets.
#List comprehension can also include an optional condition to filter the elements of the original list.

lst = [x for x in range(10)]
print(lst)
lst1 = [x*x for x in range(10) if x % 2 == 0]
print(lst1)
