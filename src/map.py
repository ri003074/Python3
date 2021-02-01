iterable = map(int, ["1", "2", "3"])

next(iterable)

for i in iterable:
    print(i)


iterable2 = map(lambda c: int(c) * int(c), ["1", "2", "3"])

print(iterable2)
for i in iterable2:
    print(i)
