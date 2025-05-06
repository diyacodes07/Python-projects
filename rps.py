import sys
import random

from enum import Enum


class RPS(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3


print("")
playerchoice = input(
    "Enter a value: \n 1 for rock \n 2 for scissors \n 3 for paper \n \n"
)
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter value 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You choose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer choose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 2:
    print("🎉You win! \n")
elif player == 2 and computer == 3:
    print("🎉You win! \n")
elif player == 3 and computer == 1:
    print("🎉You win! \n")
elif player == computer:
    print("😲Match ties! \n")
else:
    print("🐍python win! \n")
