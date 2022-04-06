import random


userChoice = int(
    input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))

computorChoice = random.randint(0, 2)
if computorChoice == 0:
    print("Computer chose rock")
elif computorChoice == 1:
    print("Computer chose paper")
else:
    print("Computer chose scissors")

if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose")
elif userChoice == 0 and computorChoice == 2:
    print("You win")
elif computorChoice == 0 and userChoice == 2:
    print("You lose")
elif computorChoice > userChoice:
    print("You lose")
elif userChoice > computorChoice:
    print("You win")
elif computorChoice == userChoice:
    print("It's a draw")
