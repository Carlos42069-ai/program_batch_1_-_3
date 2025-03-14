#Ask user for 10 numbers to put in the list
def input_numbers():
    return [int(input("Enter a number: ")) for _ in range(10)]
#Keep only the first occurrence of each number.
#Print the final list of numbers.