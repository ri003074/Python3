print(3 / 5)
print(3 // 5)
print(3 % 5)
print(5 // 5)
print(5 % 5)
print(5 / 5)
print(2 ** 2)
print(3 ** 2)


if 5 << 8 << 10:
    print("ok")


def is_leap(year):
    leap = False

    if 1900 <= year <= (10 ** 5) and (year % 400) == 0:
        leap = True

    return leap


print(is_leap(2000))
print(1992 % 400)

for i in range(3):
    print(i, end="")


s = "a b 5 1 3g"
print(type(s))


def solve(s):
    variables = s.split(" ")

    result = []
    for var in variables:
        print(var[0].upper() + var[1:])
        result.append(var[0].upper() + var[1:])

    print(" ".join(result))
    return " ".join(result)


solve(s)
name = "kenta kawamoto"
solve(name)


def solve2(s):
    return " ".join(w[:1].upper() + w[1:] for w in s.split(" "))


name = "kenta   kawamoto"
print(solve2(name))
