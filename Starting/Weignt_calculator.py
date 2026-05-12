# Weight Calculator
# conversion of weight from one unit to another 
# 1 kilo = 2.20462 pounds
# The program will ask the user to enter the weight and the unit (kilo or pound) and then it will convert the weight to the other unit and print the result.    



weight = float(input("Enter the weight: "))
unit = input("kilo or pound : ")

if unit == "k":
    weight_in_pounds = weight * 2.20462
    print(f"The weight in pounds is: {round(weight_in_pounds, 2)} kilos")
elif unit == "p":
    weight_in_kilos = weight / 2.20462
    print(f"The weight in kilograms is: {round(weight_in_kilos, 2)} pounds")
else:
    print("Invalid unit. Please enter 'kilo' or 'pound'.")

