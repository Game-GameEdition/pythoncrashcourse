def factorial (x):
    #base case
    if x <= 1:
        return 1
    else:
    #recursive case
        return x * factorial(x-1)
    
for i in range(1,11):
    print(f"{i}! = {factorial(i)}")

def fibbonaci(x):
    #base case
    if x <= 1:
        return x
    else:
        return fibbonaci(x-2) + fibbonaci(x-1)

for i in range(0,10):
    print(f"{fibbonaci(i)}")

def prepare_string(input_string):
    output_string = ""
    for c in input_string:
        if c.isalpha():
            output_string += c.lower()
    return output_string

'''
def check_palindrome(cleaned_string):
    correct_c = 0
    is_palindrome = False
    for c in range(0, int(len(cleaned_string)/2)+1):
        if c == cleaned_string[-c]:
            correct_c + 1
        else:
            return is_palindrome
    if correct_c 
'''

def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
            return is_palindrome(s[1:-1])
    else:
        return False

test_string = "Go hang a salami, I'm a lasagna hog."
print(is_palindrome(prepare_string(test_string)))

def hanoi_solver(start, end, helper, disks):
    if disks == 0:
        return
    else:
        hanoi_solver(start, helper, end, disks-1)
        print(f"Move disk from {start} to {end}")
        hanoi_solver(helper, end, start, disks-1)
    
hanoi_solver("A","C","B",2)
