#Question 1: Division Calculator

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
try:
    result = numerator / denominator
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except ValueError:
    print("Please enter valid integers for numerator and denominator, silly.")