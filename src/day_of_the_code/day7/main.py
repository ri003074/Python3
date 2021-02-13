import random

word_list = ["aardvark", "baboon", "camel"]


# chosen_word = word_list[random.randint(0, len(word_list) - 1)]

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append("_")

print(chosen_word)
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Guess: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
else:
    print("You Win!!")
