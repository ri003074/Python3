# def repeatedString(s, n):
#     words = s * n

#     # while 1:
#     #     if len(words) < n:
#     #         words += s
#     #     else:
#     #         break

#     return words[:n].count(words[0])


def repeatedString(s, n):
    n1 = s.count("a") * (n // len(s)) + s[: (n % len(s))].count("a")
    return n1


print(repeatedString("a", 100000000))
