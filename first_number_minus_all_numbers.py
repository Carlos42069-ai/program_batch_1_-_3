#Ask user for numbers' 1-10
num1 = float(input("Enter your first number "))
num2 = float(input("Enter your second number "))
num3 = float(input("Enter your third number "))
num4 = float(input("Enter your fourth number "))
num5 = float(input("Enter your fifth number "))
num6 = float(input("Enter your sixth number "))
num7 = float(input("Enter your seventh number "))
num8 = float(input("Enter your eighth number "))
num9 = float(input("Enter your nineth number "))
num10 = float(input("Enter your tenth number "))
#Define variable name and its function
one_vs_nine = num1 - (num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
#Print the results
print("The result of the first number minus all of the remaining numbers is: ", one_vs_nine)