# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = int(num1) + int(num2)
        print(f"The result is {result}")
    case "-":
        result = int(num1) - int(num2)
        print(f"The result is {result}")
    case "*":
        result = int(num1) * int(num2)
        print(f"The result is {result}")
    case "/":
        if int(num2) != 0:
            result = int(num1) / int(num2)
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected. Please choose +, -, *, or /.")
