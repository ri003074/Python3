from art import vs
from art import logo
from game_data import data
import random

print(logo)


def print_info(data):
    print(f"Compare A: {data['name']}, {data['description']}, {data['country']}")


def judge(data_a, data_b, answer):
    data_a_followers = data_a["follower_count"]
    data_b_followers = data_b["follower_count"]

    if data_a_followers > data_b_followers:
        return answer == "A"
    else:
        return answer == "B"


should_continue = True
counter = 0

while should_continue:
    compare_a_number = random.randint(0, len(data) - 1)
    compare_a_data = data[compare_a_number]
    data.pop(compare_a_number)

    print_info(compare_a_data)
    print(vs)

    compare_b_number = random.randint(0, len(data) - 1)
    data.pop(compare_b_number)
    compare_b_data = data[compare_b_number]

    print_info(compare_b_data)
    answer = input("Who has more followers? Type A or B :")
    should_continue = judge(compare_a_data, compare_b_data, answer)

    if should_continue is True:
        counter += 1
    else:
        print(f"Your score is {counter}")
