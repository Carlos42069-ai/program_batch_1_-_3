#Ask user for a first and second number
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
#Make a loop and set conditions that print "Not Equal" when numbers entered are not equal
if num1 != num2:
    print("Not Equal")

elif num1 == num2:
    print("The numbers you entered are equal")
else:
    exit
