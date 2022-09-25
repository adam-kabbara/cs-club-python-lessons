import random

commands = ["rock", "paper", "scissors"]

while True:
    user_command = input("type either rock, paper, scissors or quit to quit the game: ").lower().strip()
    if user_command == "quit":
        print("quitting game")
        break
    elif user_command not in commands:
        print("invalid command")
    else:
        computer_command = commands[random.randint(0, len(commands) - 1)]
       
        if computer_command == user_command:
            print(f"[DRAW] - you both picked {computer_command}")
        # computer wins
        elif computer_command == "scissors" and user_command == "paper":
            print(f"[COMPUTER WINS] - computer picked {computer_command} & user picked {user_command}")
        elif computer_command == "rock" and user_command == "scissors":
            print(f"[COMPUTER WINS] - computer picked {computer_command} & user picked {user_command}")
        elif computer_command == "paper" and user_command == "rock":
            print(f"[COMPUTER WINS] - computer picked {computer_command} & user picked {user_command}")
        # user wins
        elif computer_command == "rock" and user_command == "paper":
            print(f"[USER WINS] - computer picked {computer_command} & user picked {user_command}")
        elif computer_command == "paper" and user_command == "scissors":
            print(f"[USER WINS] - computer picked {computer_command} & user picked {user_command}")
        elif computer_command == "scissors" and user_command == "rock":
            print(f"[USER WINS] - computer picked {computer_command} & user picked {user_command}")


# note that this is the most straight forward way of
# programming this game, and that there are many more
# efficient ways of coding it
