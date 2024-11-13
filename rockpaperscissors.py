# class WinChecker: 
#    def compare(player, computer):
#        if player == computer
import random

def choose_random():
    return random.randint(0,2)

def get_user_input():
    valid_input = False
    user_input = input("Rock(0), paper(1), or scissors(2)? ")
    while not valid_input:
        if user_input == "0" or user_input == "1" or user_input == "2":
            valid_input = True
            return user_input, valid_input
        elif user_input.lower() =="q":
            valid_input = True
            return user_input, valid_input
        else:
            return user_input, valid_input

options = ["rock", "paper", "scissors"]

game_going = True
while game_going:
    user_input = get_user_input()
    if not user_input[1]:
        print("re-read the documentation, bucko")
        print(f"You entered: {user_input[0]}")
        continue
    if user_input[1]:
        computer_choice = choose_random()
        print(f"The computer chose: {options[computer_choice]}")
    print(f"You entered: {options[int(user_input[0])]}")

def check_win(input_1, input_2):
    diff = input_1 - input_2
    outcomes = ["no game!", "cooked gg ez", "winner winner chicken dinner",]
    print(f"{outcomes[diff % 3]}")

check_win(user_input, computer_choice)