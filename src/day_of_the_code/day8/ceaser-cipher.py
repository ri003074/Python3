alphabet = [
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
]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}")


def decode(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        print(new_position)
        cipher_text += alphabet[new_position]

    print(f"The decoded text is {cipher_text}")


# def caeser(text, shift, direction):
#     result = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position + shift
#         else:
#             new_position = position - shift
#         result += alphabet[new_position]
#     print(f"{direction} message is {result}")


def caeser(text, shift, direction):
    end_text = ""
    for letter in text:
        position = alphabet.index(letter)
        print(f"position = {position}")
        shift_amount = shift
        if direction == "decode":
            shift_amount = shift * -1
        new_position = position + shift_amount
        print(f"new position = {new_position}")
        end_text += alphabet[new_position]
    print(f"{direction} code is {end_text}")


# encrypt("hello", 5)
# decode("a", 5)
# encrypt("civilization", 5)
# encrypt("vwxyz", 5)
# caeser("hello", 5, "encode")
caeser("mjqqt", 5, "decode")
