import random

def choose_random():
    return random.randint(0,2)

def get_user_input():
    valid_input = False
    user_input = input("Rock(0), paper(1), or scissors(2)? ")
    if (user_input == "0") or (user_input == "1") or (user_input == "2") or  (user_input.lower() == "q"):
        valid_input = True
        return user_input, valid_input
    else:
        return user_input, valid_input

def check_win(input_1, input_2):
    diff = input_1 - input_2
    outcomes = ["no game!", "cooked gg ez", "winner winner chicken dinner",]
    print(f"{outcomes[diff % 3]}")

options = ["rock", "paper", "scissors"]
game_going = True

while game_going == True:
    user_input = get_user_input()
    if not user_input[1]:
        print("re-read the documentation, bucko")
        print(f"You entered: {user_input[0]}")
    elif user_input[1] == True and user_input[0].lower() == "q":
        print("thanks for playing!")
        quit()
    elif user_input[0].lower != "q" and user_input[1] == True:
        computer_choice = choose_random()
        print(f"The computer chose: {options[computer_choice]}")
        print(f"You entered: {options[int(user_input[0])]}")
        check_win(computer_choice, int(user_input[0]))