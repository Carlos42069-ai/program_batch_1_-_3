#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#Sort the numbers from highest to lowest.
#Display the sorted numbers.

def sort_numbers_descending():
    numbers = []
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid input. Stopping program.")
            break
    
    if numbers:
        numbers.sort(reverse=True)
        print("Numbers in descending order:", numbers)
    else:
        print("No valid numbers were entered.")
sort_numbers_descending()