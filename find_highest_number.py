#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#Identify and display the highest number.

def highest_number():
    numbers = []
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid input. Stopping program.")
            break
    
    if numbers:
        print("Highest number:", max(numbers))
    else:
        print("No valid numbers were entered.")

highest_number()