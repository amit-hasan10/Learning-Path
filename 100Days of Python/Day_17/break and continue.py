#The break statement in Python is used to immediately terminate the nearest enclosing for or while loop.
for i in range(12):
    print("5 X", i, "=", 5*i)
    if i ==10:
        break
print("The loop is broken")

#The continue statement in Python is used to skip the current iteration of a loop and move to the next iteration.
for i in range(12):
    if i == 10:
        print("Skipping the iteration when i is 10")
        continue
    print("5 X", i, "=", 5*i)