#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#Identify and display the number with the highest count of duplicates.

def most_frequent_number():
    numbers = []
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid input. Stopping program.")
            break
    
    if numbers:
        most_frequent = max(set(numbers), key=numbers.count)
        print("Most duplicated number:", most_frequent)
    else:
        print("No valid numbers were entered.")

most_frequent_number()
