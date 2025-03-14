#Ask user for 10 numbers to put in the list
def input_numbers():
    return [int(input("Enter a number: ")) for numero in range(10)]
#Keep only the first occurrence of each number.
def remove_duplicates(numbers):
        result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
#Print the final list of numbers.