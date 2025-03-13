#Defining even counter
even_counter = 0

#Loop runs 10 times to get 10 numbers
for ten_number in range(10):
    num = int(input(f"Enter number {ten_number+1}: "))
    if num % 2 == 0: #Checking for even numbers
        even_counter += 1
