#Ask user for two numbers
num1 = float(input("Enter your first number "))
num2 = float(input("Enter your second number "))
#Setting if else conditions and printing the remainder
if num2 !=0:
    remainder = num1 % num2
    print("The remainder is: ", remainder)

else:
    print("Please re-enter your two numbers")
