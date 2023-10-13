# calculator.py (feature-final-version branch)

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculate_percentage(x, percentage):
    return (x * percentage) / 100

def square_root(x):
    return math.sqrt(x)

def calculate_remainder(x, y):
    if y == 0:
        return "Cannot calculate remainder when the divisor is zero"
    return x % y

print("Welcome to the Calculator (Final Version)")

while True:
    print("\nOptions:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'percentage' for percentage calculation")
    print("Enter 'square_root' for square root calculation")
    print("Enter 'remainder' for remainder calculation")
    print("Enter 'exit' to end the program")

    user_input = input("enter number : ")

    if user_input == "exit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "percentage", "square_root", "remainder"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
        elif user_input == "percentage":
            print("Result:", calculate_percentage(num1, num2))
        elif user_input == "square_root":
            print("Result:", square_root(num1))
        elif user_input == "remainder":
            print("Result:", calculate_remainder(num1, num2))
    else:
        print("Invalid input. Please try again.")
