lst = [1, 20, 2, 3, 5]
print(lst)
print(type(lst))


print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[2:4])
print(lst[2:])
print(lst[:3])
print(len(lst))

moji = "abcdefg"
list = list(moji)
print(list)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

a = ["a", "b", "c"]
n = ["x", "y", "z"]
x = [a, n]
print(x)

s = ["a", "b", "c", "d", "e", "f", "g"]

print(s)
print(s[2:5])
s[2:5] = []
print(s)
s[:] = []
print(s)

n = [1, 2, 3]
n.append(4)
print(n)
n.insert(0, 200)
print(n)
print(n.pop())
print(n.pop(0))

n.remove(2)
print(n)

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)
r = [1, 2, 3, 4, 5, 6, 7, 3]
print(r.index(3))
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print("exist")


r.sort()
print(r)
r.reverse()
print(r)

s = "My name is kenta"
to_split = s.split(" ")
print(to_split)

x = " ".join(to_split)
print(x)
# print(help(list))

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print("i = ", i)
print("j = ", j)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 10j

print("x = ", x)
print("y = ", y)


x = 20
y = x
y = 5
print(id(x))
print(id(y))

print(x)
print(y)


X = [1, 2]
Y = X
Y[0] = 3


print(id(X))
print(id(Y))
print(X)
print(Y)
