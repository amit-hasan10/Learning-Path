#Length of String
x = "Hello, World!"
print(len(x))  # Output: 13

fruit = "Banana"
len1 = len(fruit)
print("Banana is a", len1, "letter word.")  # Output: Banana is a 6 letter word.

#String Slicing
name = "Amit, Kumar Singh"
print(name[0:4])        # Output: Amit #including index 0 to 3
print(name[6:10])       # Output: Kumar #including index 6 to 9 #including start index and excluding end index
print(name[:4])         # Output: Amit #from beginning to index 3
print(name[6:])         # Output: Kumar Singh #from index 6 to end
print(name[-5:-1])      # Output: ingh #including index -5 to -2 #including start index and excluding end index
print(name[-5:])        # Output: Singh #
print(name[:-5])        # Output: Amit, Kumar
b = "Hello, World!"
print(b[-5:-2])
c = "Amity"
print(c[-4:-2])