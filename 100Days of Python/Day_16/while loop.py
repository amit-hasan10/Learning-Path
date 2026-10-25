#With the while loop we can execute a set of statements as long as a condition is true

i = int(input("Enter a number: "))
while i < 10:
    print(i)
    i += 1
print("The while loop is over")

j = 0
while j <= 5:
    print(j)
    j +=1
else:
    print("The loop successfully completed")

#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("The loop is broken")

#With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)