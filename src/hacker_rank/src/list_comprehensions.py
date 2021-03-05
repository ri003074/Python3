# a = 2
# b = 2
# c = 2
# n = 2

a = 1
b = 1
c = 1
n = 2

result = [
    [x, y, z]
    for x in range(a + 1)
    for y in range(b + 1)
    for z in range(c + 1)
    if (x + y + z != n)
]
print(result)
