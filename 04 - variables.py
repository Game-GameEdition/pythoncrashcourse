# variables are one of the most essential parts of any programming language.
# a variable holds a value, then instead of using that value, the variable can be used to represent it.
# a variable declaration involves writing the variable name on the left, equals sign in the middle, and the value on the right

x = "Hello,"
y = "World!"

print(x,y)

# as you can see the x and y are the variable names, neither of which are surrounded by parenthesis. However, the value on the right does have parenthesis.

# Run the script and see what happens.

# try adding a new variable z. Make sure you declare z above the print statement

z = "I am python."

# Then change the print to print(x,y,z)

print(x,y,z)

# What prints out?
# What if we declare a variable from another variable? What if you write:
x = "Hello,"
y = "World!"
z = y
print(x,y,z)
# What prints now?

# You should see "Hello World World". This is because a variable can also be assigned from another variable! Notice that, in this case the y didn't have quotation marks around it even though it was on the right side.

# What happens if we do use quotation marks?
# x = "Hello"
# y = "World"
z = "y"
print(x,y,z)
# What prints now?

# You should see "Hello World y". This is because the y is not actually the variable y, but instead just the value of y. You'll see more about this in the next section.

# BREAK IT:
# What happens if you try to use a number as a variable name?
# For example: 
# 1 = "Hello"
10 = "i am breaking the code!"
print(10)
# Why do you think the error occurs?
# A: it doesn't make sense to the interpreter. the actual numerical value 10 (represented in binary as 1010) is different
# from variable names (such as "user_name", "updated_version", "home_distance") that can represent strings. 10 is already
# its own thing (an integer)