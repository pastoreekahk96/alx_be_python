"""
Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script.
"""


def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2

    return "Error: Invalid operation"
