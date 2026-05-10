#typecasting is the process of converting a variable from one type to another. In Python, you can use built-in functions to perform typecasting. Here are some common typecasting functions:
# int(): Converts a value to an integer.
# float(): Converts a value to a floating-point number.
# str(): Converts a value to a string.
# bool(): Converts a value to a boolean.
# Example of typecasting:
name = "Alice"
age = 30
gpa = 3.5
is_student = True

gpa_str = str(gpa)  # Convert float to string
age_float = float(age)  # Convert integer to float
is_student_int = int(is_student)  # Convert boolean to integer
age_str = str(age)  # Convert integer to string
print(type(gpa_str))  # Output: <class 'str'>
print(type(age_float))  # Output: <class 'float'>
print(type(is_student_int))  # Output: <class 'int'>
print(type(age_str))  # Output: <class 'str'>

name_str = str(name)  # Convert string to string (no change)
name_bool = bool(name)  # Convert non-empty string to boolean (True)
print(type(name_str))  # Output: <class 'str'>
print(type(name_bool))  # Output: <class 'bool'>
names = ""
names_str = bool(names)  # Convert empty string to boolean (False)
print(type(names_str))  # Output: <class 'bool'>
# In this code, we have a string variable name, an integer variable age, a float variable gpa, and a boolean variable is_student. We use typecasting functions to convert these variables to different types. We then print the type of each converted variable to verify the typecasting.