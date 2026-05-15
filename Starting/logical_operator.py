# logical operators = used to combine conditional statements 
# and = both conditions must be true
# or = one of the conditions must be true
# not = reverses the result, returns false if the result is true

temp = int(input("what is the temperature outside? "))

if temp >= 0 and temp <= 30: # 
    print("the temperature is good today")
    print("go outside")
elif temp < 0 or temp > 30: # this is the same as not (temp >= 0 and temp <= 30)
    print("the temperature is bad today")
    print("stay inside")
elif temp >= 0 and not temp <= 30:   # this is the same as temp > 30
    print("the temperature is bad today")
    print("stay inside")
else:
    print("enter a valid number")
