import random
from replit import clear
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def select_card():
    return cards[random.randint(0, len(cards) - 1)]  # could use random.choice


def calc_score(hands):
    return sum(hands)


def judge_continue():
    playing_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if playing_flag == "n":
        return False
    return True


should_continue = judge_continue()
while should_continue:
    clear()
    your_cards = []
    computer_cards = []
    your_score = 0
    computer_score = 0

    for i in range(2):
        your_cards.append(select_card())
        computer_cards.append(select_card())

    your_score = calc_score(your_cards)
    print(f"Your cards: {your_cards}, current_score: {your_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    continue_flag = input("Type 'y' to get another card, type 'n' to pass: ")

    if continue_flag == "y":
        your_cards.append(select_card())

    your_score = calc_score(your_cards)
    computer_score = calc_score(computer_cards)
    print(f"Your cards: {your_cards}, current_score: {your_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    print(f"Your cards: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if your_score > computer_score:
        print("You win")
    elif your_score < computer_score:
        print("You loose")
    else:
        print("draw")

    should_continue = judge_continue()
