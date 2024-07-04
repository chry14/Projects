import sys
import random

player = input("Pick a number! \n 1. For Rock \n 2. For Paper \n 3. For Scissors \n 4. For Nuke \n\n")

playerchoice = int(player)

if playerchoice < 1 | playerchoice > 5:
    sys.exit("You must pick 1, 2, 3, or 4")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + player)
print("the CPU chose " + computerchoice)
print("")
if playerchoice == 4:
    print("Both of you died!")
elif computer == 1 and playerchoice == 3:
    print("The CPU won!")
elif computer == 2 and playerchoice == 3:
    print("You won!")
elif computer == 3 and playerchoice == 3:
    print("Tie!")
elif computer == 1 and playerchoice == 2:
    print("You won!")
elif computer == 3 and playerchoice == 2:
    print("The CPU won!")
elif computer == 2 and playerchoice == 2:
    print("Tie!")
elif computer == 2 and playerchoice == 1:
    print("The CPU won!")
elif computer == 3 and playerchoice == 1:
    print("You won!")
elif computer == 1 and playerchoice == 1:
    print("Tie!")

