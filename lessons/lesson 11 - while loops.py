# while loops allow us to iterate as long a condition is true
# while condition == True:
#    (some code)

i = 0
while i < 10:
    print(i)
    i = i+1

# you can also use the break keyword in while loops
i = 0
while True:
    print("run")
    if i == 10:
        break
    i = i+1

# excersise 6
# create a text base rock paper scissors game
# that keeps on going until you type "quit"
import random
moves = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(moves) 
    user = input("enter a move (rock paper or scissors): ")
    if computer == user:
        pass