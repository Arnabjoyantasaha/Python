# python calculator
# This program performs basic arithmetic operations based on user input.
#result is rounded to 3 decimal places for better readability.
# The program also includes error handling for division by zero and invalid operators.

operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = round(num1 + num2)
    print(f"{num1} + {num2} = {result, 3}")
elif operator == "-":
    result = round(num1 - num2)
    print(f"{num1} - {num2} = {result, 3}")
elif operator == "*":
    result = round(num1 * num2)
    print(f"{num1} * {num2} = {result, 3}")
elif operator == "/":
    if num2 != 0:# Check for division by zero before performing the division 
        result = round ( num1 / num2 )
        print(f"{num1} / {num2} = {result, 3}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")

