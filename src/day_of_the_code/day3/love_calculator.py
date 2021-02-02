name1 = "Angela Yu"
name2 = "Jack Bauer"
name = name1 + name2


def count(str):
    total = 0
    for word in str:
        counter = name.lower().count(word.lower())
        print(f"{word} occur {counter} ")
        total += counter
    print(f"Total = {total}")
    return total


total = str(count("TRUE")) + str(count("LOVE"))
print(f"Print: Your score is {total}")
