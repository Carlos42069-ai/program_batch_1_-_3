#Define variable name for counting odd number
odd_number_count = 0
#Set conditions for counting odd number
for ten_numbers in range(10):
    num = int(input(f"Enter a number {ten_numbers+1}:"))
    if num % 2 != 0: #first commit have extra space and made an error, added a colon to run the program correctly
        odd_number_count +=1
#Print the total odd number counted
print("The total odd number is: ", odd_number_count)