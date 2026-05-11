# This code demonstrates the use of if-else statements in Python to make decisions based on certain conditions.
# if = do something if a condition is true
# else = do something if the condition is false
# elif = do something if the previous conditions were false and this condition is true
#

is_student = True
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
# In this code, we have a boolean variable is_student that indicates whether the person is a student or not. We use an if-else statement to check the value of is_student. If it is True, we print "You are a student." Otherwise, we print "You are not a student." In this case, since is_student is set to True, the output will be "You are a student."


is_online = False
if is_online:
    print("You are online.")
else:
    print("You are offline.")
# In this code, we have a boolean variable is_online that indicates whether the person is online or not. We use an if-else statement to check the value of is_online. If it is True, we print "You are online." Otherwise, we print "You are offline." In this case, since is_online is set to False, the output will be "You are offline."


age = 20
if age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You are Dead.")
else: 
    print("You are a minor.")
# In this code, we have an integer variable age that represents a person's age. We use an if-else statement to check if the age is greater than or equal to 18. If it is, we print "You are an adult." Otherwise, we print "You are a minor." In this case, since age is set to 20, the output will be "You are an adult."


name = input("Enter your name: ")
if name == "":  # Check if the name is an empty string
    print("You didn't enter your name.")
else:
    print("You didn't enter your name.")
# In this code, we use the input() function to prompt the user to enter their name. We then check if the name is an empty string (i.e., if the user didn't enter anything). If the name is empty, we print "You didn't enter your name." Otherwise, we also print "You didn't enter your name." In this case, since both conditions lead to the same output, it will always print "You didn't enter your name." regardless of the user's input.