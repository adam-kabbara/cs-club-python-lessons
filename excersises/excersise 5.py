import random
# returns a random # btwn 1 and 10 inclusive
secrete_number = random.randint(1, 10)

trials = 3
player_won = False

for i in range(trials):
    guess = int(input("enter a number btwn 1 and 10: "))
    if guess == secrete_number:
        print("YOU HAVE GUESSED THE NUMBER!!")
        print(f"it took you {trials} trials")
        player_won = True
        break
    elif guess > secrete_number:
        print("guess a lower number")
    else:
        print("guess a higher numeber")

if not player_won:
    print("YOU HAVE LOST THE GAME")
    print(f"the secrete number was {secrete_number}")
