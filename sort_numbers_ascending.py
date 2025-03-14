#Continuously ask the user to input a number.
#If the input is invalid (non-numeric), stop asking for input.
#Store valid numbers in a list.
#After input ends, sort the numbers from lowest to highest.
#Display the sorted numbers.
def getting_the_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Stopping program.")
            break
    
    if numbers:
        numbers.sort()
        print("Numbers in order:", numbers)
    else:
        print("No valid numbers were entered.")
        
getting_the_numbers()