"""
Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script

"""
def perform_operation(num1, num2, operation):
    if opperation == 'add':
        return num1 + num2

    elif opperation == 'subtract':
        return num1 - num2

    elif opperation == 'multiply':
        return num1 * num2

    elif opperation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2

    else:
        return "Error: Invalid opperation"
