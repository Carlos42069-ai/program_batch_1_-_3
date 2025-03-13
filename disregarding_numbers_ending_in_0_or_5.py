#Make a loop that goes through 0 to 100 
num = 0
while num <= 100:  
    if num == 0 or (num % 10 != 0 and num % 10 != 5): #Skip multiples of 10 and 5
#Print the results of the loop if condition is fulfilled
        print(num)
    num += 1 #Counts 1-100 with certain conditions 
