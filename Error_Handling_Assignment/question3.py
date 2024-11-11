#Question 4: Integer Conversion

user_input = input("Enter a number: ")
try:
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)
except ValueError:
    print("Heyya, Please enter a valid integer.")