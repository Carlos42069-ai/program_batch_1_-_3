#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#After each input, check if the number has appeared before.
# Display "Unique" if the number appears for the first time, otherwise display "Duplicate".
def getting_the_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number: "))
            if num in numbers:
                print("Duplicate")
            else:
                print("Unique")
                numbers.append(num)
        except ValueError:
            print("Invalid input detected. Closing the program.")
            break

getting_the_numbers()