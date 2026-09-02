import random
Player = 0
computer = 0
variants = ["scrissors", "paper", "rock"]
print(f"welcome to the game, chose one of the variants {variants}")
Player_variant = None
while Player != 3 and computer != 3:
    Player_variant = input("chose: ").lower()
    if Player_variant not in variants:
        print("Please print else")
    else:
        computer_variant = (random.choice(variants))
        print(f" computer choice: {computer_variant}")
        if Player_variant == computer_variant:
            print("it's a tie, try again")
        elif Player_variant == "scrissors" and computer_variant == "paper" or\
            Player_variant == "rock" and computer_variant == "scrissors" or\
            Player_variant ==  "paper" and computer_variant == "rock":
                print(" player get 1 score")
                Player += 1
                print("player:", Player)
                print("computer:", computer)
        else:
            print(" computer get 1 score")
            print("player:", Player)
            computer += 1
            print("computer:", computer)
if computer == 3:
   print(" you lost, don't worry try again")
elif Player == 3:
   print(" you win, hat off")
