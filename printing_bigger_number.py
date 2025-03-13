#Ask User to input two numbers

num1 = int(input("Enter the first number: "))  
num2 = int(input("Enter the second number: "))  

#Swapping Values when num1 is bigger than num2

if num1 > num2:
    num1, num2 = num2, num1  

#Looping between numbers

for num in range(num1 + 1, num2):  
    print(num)  