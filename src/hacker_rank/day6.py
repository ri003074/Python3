s = "abcdef"

for i in range(0, len(s) - 1, 2):
    print(s[i], end="")
print(" ", end="")

for i in range(1, len(s), 2):
    print(s[i], end="")
print("")


print(*["1", "2", "3"])
print(*"".join(s[::2]))
print(s[::2], s[1::2])

for i in range(int(input())):
    s = input()
    # print(*["".join(s[::2]), "".join(s[1::2])])
    print(s[::2], s[1::2])
