x = int(input("Enter a number: "))
match x:
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 4:
        print("X is 4")
    case _ if x!=90:
        print(x, "is not equal to 90")
    case _ if x!=80:
        print(x, "is not equal to 80")


'''Combine Values
Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case'''
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

#Add if statements in the case evaluation as an extra condition-check
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

#Pracatice

month = 3
day =10
match day:
     case 1|2|3|4|5 if month == 3:
            print("My Birthday is not in there")
     case 1|5|7|10 if month ==3:
            print("My Birthday is in there")
