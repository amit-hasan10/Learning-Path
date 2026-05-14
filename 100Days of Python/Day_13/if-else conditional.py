a = int(input("Enter a number: "))
print("Your number is: ", a)
if a>18:
    print("You are an adult.")
else:
    print("You are a minor.")
a = 20
b = 10
if a > b:
    print("a is greater than b.")
else:
    print("a is not greater than b.")

#el-if statement
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num==0:
    print("The number is zero.")
elif num==99:
    print("The number is special")
else:
    print("The number is negative.")
print("I am happy")

num1= 17
if num1<0:
    print("The number is negative.")
elif num1>0:
    if num1<=10:
        print("The number is positive and less than or equal to 10.")
    elif num1>10 and num1<=20:
        print("The number is positive and between 11 and 20.")
    else:
        print("The number is positive and greater than 20.")
else:
    print("The number is zero.")
