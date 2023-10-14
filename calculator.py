import tkinter as tk
from tkinter import ttk
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

def calculate_power(x, y):
    return math.pow(x, y)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create labels and entry fields
label_1 = ttk.Label(window, text="Enter the first number:")
label_1.grid(row=0, column=0)
entry_1 = ttk.Entry(window)
entry_1.grid(row=0, column=1)

label_2 = ttk.Label(window, text="Enter the second number:")
label_2.grid(row=1, column=0)
entry_2 = ttk.Entry(window)
entry_2.grid(row=1, column=1)

result_label = ttk.Label(window, text="Result:")
result_label.grid(row=2, column=0, columnspan=2)

def calculate():
    num1 = float(entry_1.get())
    num2 = float(entry_2.get())
    operation = operation_var.get()

    if operation == "add":
        result_label.config(text="Result: " + str(add(num1, num2)))
    elif operation == "subtract":
        result_label.config(text="Result: " + str(subtract(num1, num2)))
    elif operation == "multiply":
        result_label.config(text="Result: " + str(multiply(num1, num2)))
    elif operation == "divide":
        result_label.config(text="Result: " + str(divide(num1, num2)))
    elif operation == "percentage":
        result_label.config(text="Result: " + str(calculate_percentage(num1, num2)))
    elif operation == "square_root":
        result_label.config(text="Result: " + str(square_root(num1)))
    elif operation == "remainder":
        result_label.config(text="Result: " + str(calculate_remainder(num1, num2)))
    elif operation == "power":
        result_label.config(text="Result: " + str(calculate_power(num1, num2))

operation_var = tk.StringVar()
operation_var.set("add")

operation_label = ttk.Label(window, text="Select operation:")
operation_label.grid(row=3, column=0)
operation_menu = ttk.OptionMenu(window, operation_var, "add", "add", "subtract", "multiply", "divide", "percentage", "square_root", "remainder", "power")
operation_menu.grid(row=3, column=1)


calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2)

window.mainloop()

