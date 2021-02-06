import random

rock = 1
paper = 2
sissors = 3

your_hand = 1

computer_hand = random.randint(1, 3)


if your_hand == 1 and computer_hand == 3:
    print("you win")

else:
    print("you lose")
