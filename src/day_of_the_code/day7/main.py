import random

from hangman_art import stages, logo
from hangman_words import word_list

lives = 6


# chosen_word = word_list[random.randint(0, len(word_list) - 1)]

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append("_")

print(logo)
print(chosen_word)
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Guess: ").lower()

    if guess in display:
        print(f"You already entered{guess}")

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    if guess not in chosen_word:
        lives -= 1

    print(display)
    print(stages[6 - lives])

    if "_" not in display or lives == 0:
        end_of_game = True
else:
    if lives > 0:
        print("You Win!!")
    else:
        print("You lose")
