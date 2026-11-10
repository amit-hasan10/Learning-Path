l = [1, 2, 3, 4, 5]
l.append(6) #adds 6 at the end of the list
print(l)
#Sort
l1 = [3,8,2,9,1,99]
l1.sort() #sorts the list in ascending order
print(l1)
l1.sort(reverse=True) #sorts the list in descending order
print(l1)
v=l1.index(9) #returns the index of the first occurrence of 9 in the list
print(v)
#Count
l2 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
print(l2.count(1)) #returns the number of occurrences of 1 in the list

l = [1, 2, 3, 4, 5]
m = l
m[0] = 100
print(l) #prints [100, 2, 3, 4, 5] because m is a reference to l

#Again
l = [1, 2, 3, 4, 5]
m = l.copy() #creates a copy of l and assigns it to m
m[0] = 100
print(l) #prints [1, 2, 3, 4, 5] because m is a copy of l
#Insert
l = [1, 2, 3, 4, 5]
l.insert(2, 100) #inserts 100 at index 2
print(l)
m = [6,7,8]
l.extend(m) #adds all elements of m to the end of l
print(l)

k = l+m #concatenates l and m and assigns it to k
print(k)
