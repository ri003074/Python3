import random

rock = 1
paper = 2
sissors = 3

your_hand = 1

computer_hand = random.randint(1, 3)

print(f"compputer choice {computer_hand}")

if your_hand == 1 and computer_hand == 3:
    print("you win")

elif your_hand == 2 and computer_hand == 1:
    print("you win")

elif your_hand == 3 and computer_hand == 2:
    print("you win")

elif your_hand == computer_hand:
    print("It's draw")

else:
    print("you lose")
