n = 5

# print(bin(n).replace("0b", ""))
# print(bin(13).replace("0b", ""))
# print(bin(13).replace("0b", ""))


def func(num):
    return num[2:]


n = 13

a = max(func(bin(n)).split("0")).count("1")
print(a)
print(max(bin(n).replace("0b", "").split("0")).count("1"))
