a = {
    1,
    2,
    3,
    3,
    3,
    3,
    3,
    2,
}
print(a)
print(type(a))

b = {2, 3}

print(a & b)

b.add(6)
print(b)

b.remove(6)
print(b)

# help(set)


my_friends = {"A", "B", "C"}
A_friends = {"X", "B", "Y"}
print(my_friends & A_friends)
