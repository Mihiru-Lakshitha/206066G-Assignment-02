
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

print("Welcome to the Calculator")


