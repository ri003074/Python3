from replit import clear
from art import logo

print(logo)

result = {}

should_input = True
while should_input:
    username = input("name?: ")
    bid = int(input("$: "))
    result[username] = bid

    should_continue = input("next? yes or no : ")
    if should_continue == "yes":
        clear()
    else:
        should_input = False


def find_highest_bidder(record):
    highest_bid = 0
    winner = ""
    for name in record:
        if record[name] > highest_bid:
            winner = name
            highest_bid = record[name]
    print(winner)


find_highest_bidder(result)
