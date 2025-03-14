#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for the input.
#Store valid numbers in a list.
#After input ends, display the lowest number from the list.
def getting_the_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input detected. Stopping the program.")
            break
    
    if numbers:
        print("Lowest number:", min(numbers))
    else:
        print("No valid numbers were entered.")

getting_the_numbers()