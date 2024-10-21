# let's learn a bit about functions.


# A function is defined in python with "def" in front, then the name of the function and an open and closed parenthesis and a colon

def hello_world():
    # In Python, indentation is very important.
    # print is indented to indicate it is inside of the hello_world() function
    print("Hello World")


# Great! we have a function, but what do we do with it?
# We can call it! To call the function, simply write the name of the function with () in front

hello_world()

# this calls the hello world function
# Also note that this is no longer indented, indicating we are now back outside of the function.

# run the program and you should see "Hello World"
# Again, you can change the print statement, and it should reflect however you changed it.

def hello_world():
    credit_card = input("Give me your credit card numbers so I can give you money! \nInput here: ")
    print("Is this correct? " + credit_card)

hello_world()

# BREAK IT:
# What happens if you move the hello_world() call above the definition of hello_world?
# Test and see. Why do you think the error occurs?
# Error: it uses the old definition of the hello_world() function, and asks twice (for the credit card)


hello_world()

def hello_world():
    print("Hello, World!")