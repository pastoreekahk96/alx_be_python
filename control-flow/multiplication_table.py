# This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

number = input("Enter a number to see its multiplication table:")

for i in range(1, 11):
    product = int(number) * i
    print(f"{number} x {i} = {product}")