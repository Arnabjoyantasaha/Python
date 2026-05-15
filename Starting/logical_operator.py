# logical operators = used to combine conditional statements 
# and = both conditions must be true
# or = one of the conditions must be true
# not = reverses the result, returns false if the result is true

temp = int(input("what is the temperature outside? "))

is_sunny = True

if temp >= 28 and is_sunny:
    print("the event is not cancelled")
if temp >= 28 and not is_sunny:
    print("the event is not cancelled")
elif temp >= 28 or is_sunny:
    print("the event is not cancelled")

else:    print("the event is cancelled")




