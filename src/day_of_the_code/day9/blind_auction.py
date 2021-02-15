from replit import clear
from art import logo

print(logo)

result = {}

should_input = True
while should_input:
    username = input("name? : ")
    bid = int(input("$ : "))
    result[username] = bid

    should_continue = input("next? yes or no : ")
    if should_continue == "yes":
        clear()
    else:
        should_input = False


winner = username

for name in result:
    if result[name] > result[winner]:
        winner = name

print(winner)
