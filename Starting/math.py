import math
# import is a keyword in Python that allows you to include external modules or libraries in your code. in this case, we are importing the math module, which provides various mathematical functions and constants.
# import math allows us to use functions like math.sqrt(), math.sin(), math.cos(), and constants like math.pi, math.e in our code.


x = 3.14
y = -4
z = 5

# round
result = round(x)
# round is a built-in function that rounds a number to the nearest integer. if the fractional part is 0.5 or greater, it rounds up; otherwise, it rounds down.
print(result)  # Output: 3

# abs
result = abs(y)
# abs is a built-in function that returns the absolute value of a number. it removes the negative sign if the number is negative, and returns the number itself if it is positive or zero.
print(result)  # Output: 4

# po
result = pow(z, 2)
# pow is a built-in function that takes two arguments: the base and the exponent. it returns the result of raising the base to the power of the exponent. in this case, it calculates 5 raised to the power of 2, which is 25.
print(result)  # Output: 25

#max
result = max(x, y, z)
# max is a built-in function that takes multiple arguments and returns the largest one. in this case, it compares 3.14, -4, and 5, and returns 5 as the largest value.
print(result)  # Output: 5

# min
result = min(x, y, z)
# min is a built-in function that takes multiple arguments and returns the smallest one. in this case, it compares 3.14, -4, and 5, and returns -4 as the smallest value.
print(result)  # Output: -4

##########################################################################################################################################################################################

# Additional functions and constants from the math module:
a = 9.4
print(math.pi)  # Output: 3.141592653589793
# math.pi is a constant in the math module that represents the value of pi, which is the ratio of a circle's circumference to its diameter. it is approximately equal to 3.14159.

print(math.e) # Output: 2.718281828459045
# math.e is a constant in the math module that represents the value of Euler's number, which is the base of the natural logarithm. it is approximately equal to 2.71828.

print(math.sqrt(16))  # Output: 4.0
# math.sqrt() is a function in the math module that calculates the square root of a number. in this case, it calculates the square root of 16, which is 4.0.

print(math.ceil(a))  # Output: 10
# math.ceil() is a function in the math module that returns the smallest integer greater than or equal to a number. in this case, it returns 10, which is the smallest integer greater than or equal to 9.4.

print(math.floor(a))  # Output: 9
# math.floor() is a function in the math module that returns the largest integer less than or equal to a number. in this case, it returns 9, which is the largest integer less than or equal to 9.4

