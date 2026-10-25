'''
A function is a block of code which only runs when it is called
A function can return data as a result
A function helps avoiding code repetition'''
def calculate_mean(a,b):
    mean = (a + b) / 2
    print(mean)

a = 7
b = 9
calculate_mean(a,b)

def isgreater(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")

c = 10
d = 5
isgreater(c,d)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)
e = 98.6
fahrenheit_to_celsius(e)