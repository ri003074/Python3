# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = 10  # int(input("How many letters would you like in your password?\n"))
nr_numbers = 3  # int(input(f"How many numbers would you like?\n"))
nr_symbols = 3  # int(input(f"How many symbols would you like?\n"))

password_letters = []
for i in range(nr_numbers):
    password_letters.append(numbers[random.randint(0, len(numbers) - 1)])


for i in range(nr_symbols):
    password_letters.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(nr_letters - nr_numbers - nr_symbols):
    password_letters.append(
        letters[random.randint(0, nr_letters - nr_numbers - nr_symbols - 1)]
    )


my_password = ""
for i in range(len(password_letters)):
    random_num = random.randint(0, len(password_letters) - 1)
    my_password += password_letters[random_num]
    password_letters.pop(random_num)


print(my_password)


password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char

print(password)
