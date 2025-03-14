#Ask user for 10 numbers to put in the list
def input_ten_numbers():
    return [int(input("Enter a number: ")) for numero in range(10)]
#Define a function to find and return numbers that appear only once in the list.
def finding_unique(numbers):
        return [num for num in numbers if numbers.count(num) == 1]

#Get user input by calling the input function.
numbers = input_ten_numbers()
#Identify unique numbers using the second function.
unique_numbers = finding_unique(numbers)
#Print the unique numbers.
