#input() = a function that allows user input data and returns it as a string
name = input("Enter your name: ")  # Prompt the user to enter their name
age = input("Enter your age: ")  # Prompt the user to enter their age
print("Your name is:", name)  # Print the user's name
print("Your age is:", age)  # Print the user's age

#excercise 1 Rectangle area calculation
length = input("Enter the length of the rectangle: ")  # Prompt the user to enter the length of the rectangle
# or length = float(input("Enter the length of the rectangle: "))  # Prompt the user to enter the length of the rectangle and convert it to a float
width = input("Enter the width of the rectangle: ")  # Prompt the user to enter the width of the rectangle
# or width = float(input("Enter the width of the rectangle: "))  # Prompt the user to enter the width of the rectangle and convert it to a float
#need to convert the input strings to float using Python's float() function to perform mathematical operations
area = float(length) * float(width)  # Calculate the area of the rectangle
# or area = length * width  # Calculate the area of the rectangle if length and width were already converted to floats
print(f"The area of the rectangle is: {area} cm²")  # Print the area of the rectangle
# for windows : Numlock + Alt + 0 1 7 6 is the shortcut for the degree symbol (°) in Python.
# for windows : Numlock + Alt + 0 1 7 8 is the shortcut for the squared symbol (²) in Python.

# Excercise 2 shopping cart Program
item = input("Enter the item you want to purchase: ")  # Prompt the user to enter the item they want to purchase
# or item = input("Enter the item you want to purchase: ")  # Prompt the user to enter the item they want to purchase and convert it to a string (though input() already returns a string)
price = input("Enter the price of the item: ")  # Prompt the user to enter the price of the item
# or price = float(input("Enter the price of the item: "))  # Prompt the user to enter the price of the item and convert it to a float
quantity = input("Enter the quantity of the item: ")  # Prompt the user to enter the quantity of the item
# or quantity = int(input("Enter the quantity of the item: "))  # Prompt the user to enter the quantity of the item and convert it to an integer
total_cost = float(price) * int(quantity)  # Calculate the total cost of the purchase
# or total_cost = price * quantity  # Calculate the total cost of the purchase if price and quantity were already converted to float and int respectively
print(f"The total cost of purchasing {quantity} {item} is: ${total_cost}")  # Print the total cost of the purchase, formatted to include the item and quantity
