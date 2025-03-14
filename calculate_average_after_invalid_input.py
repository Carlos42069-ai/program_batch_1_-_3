#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#Calculate the average of the numbers.
#Display the average.

def calculate_average():
    numbers = []
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid input. Stopping program.")
            break
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print("Average:", average)
    else:
        print("No valid numbers were entered.")
calculate_average()