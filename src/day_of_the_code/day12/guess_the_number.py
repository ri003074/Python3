from art import logo
import random


correct_answer = random.randint(1, 100)

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
print(f"Press, the correct answer is {correct_answer}")
level = input("type 'easy' or 'hard':")


attemts_remaining = 0
if level == "easy":
    attemts_remaining = 10
else:
    attemts_remaining = 5


game_is_over = False

while not game_is_over:
    print(f"You can {attemts_remaining} attempts")
    guess_answer = int(input("make a guess: "))
    if guess_answer == correct_answer:
        print(f"You got it. that wass {correct_answer}")
        game_is_over = True
    elif guess_answer > correct_answer:
        print("Too high")
        attemts_remaining -= 1

    elif guess_answer < correct_answer:
        print("Too low")
        attemts_remaining -= 1

    if attemts_remaining == 0:
        game_is_over = True
