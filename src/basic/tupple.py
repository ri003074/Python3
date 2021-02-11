t = (1, 2, 3, 4, 1, 2)
print(type(t))


# error
# t[0] = 1

p = 1, 2
print(type(p))
q = (1,)
print(type(q))


num_tupple = (10, 20)
print(num_tupple)

x, y = num_tupple
print(x, y)

# not good example hard to read
a, b, c = "Mike", "desu", "yo"

a = "Mike"
b = "desu"

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
