#variable = A container for a value( strings, integer, float, boolean, etc.)
# A variable behaves like a container that holds data. When you create a variable, you can assign it a value, and then use that variable to access or manipulate the data stored in it.
# In Python, you can create a variable by simply assigning a value to it using the equals sign (=). For example:

x = 5
print(x)  # Output: 5
print("x")  # Output: x
# In this example, we created a variable named x and assigned it the value of 5. We can then print the value of x, which outputs 5. If we print "x" (with quotes), it will output the string "x" instead of the value stored in the variable.
# You can also change the value of a variable by assigning a new value to it. For example:
x = 10
print(x)  # Output: 10
# In this example, we reassigned the variable x to a new value of 10. When we print x again, it outputs the updated value of 10.
# Variables can hold different types of data, such as strings, integers, floats, and booleans. For example:
name = "Bro"

age = 30

height = 1.75756

is_student = True

print(name)  # Output: Bro
print(type(name))  # Output: <class 'str'>
#type() function is used to check the data type of a variable. In this case, it shows that name is of type 'str' (string).
print(f"Hello, {name}!")  # Output: Hello, Bro!
#formatting strings, we can use f-strings (formatted string literals) to embed variables directly within a string. By prefixing the string with 'f' and using curly braces {}, we can include the variable name inside the string, and it will be replaced with the variable's value when printed.

print(age)   # Output: 30
print(type(age))  # Output: <class 'int'>

print(height)  # Output: 1.75756
print(f"Height: {height:.2f}")  # Output: Height: 1.76
# In this example, we are using string formatting to display the height variable with 2 decimal places.
print(type(height))  # Output: <class 'float'>

print(is_student)  # Output: True
print(type(is_student))  # Output: <class 'bool'>

# In this example, we created variables of different data types (string, integer, float, and boolean) and printed their values and types.
