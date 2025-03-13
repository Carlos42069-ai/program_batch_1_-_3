#Make a code that skip numbers ending in 0
for number in range(101): #Count 0 to 100
    if number % 10 != 0: #Specific code that checks if number is not a multiple of 10
        print(number) #Prints numbers