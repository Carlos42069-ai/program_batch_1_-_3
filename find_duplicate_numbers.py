#Ask the user to input 10 numbers.
#Store the numbers in a list.
#Identify numbers that appear more than once.
#Display only the duplicate numbers.

def getting_the_duplicates():
    numbers = [int(input("Enter a number: ")) for _ in range(10)]
    duplicates = sorted(set(num for num in numbers if numbers.count(num) > 1))
    
    if duplicates:
        print("Duplicate numbers:", duplicates)
    else:
        print("No duplicate numbers found.")

getting_the_duplicates()