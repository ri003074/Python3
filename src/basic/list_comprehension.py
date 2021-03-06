"""
list comprehension is used for when create a new list

new_list = [new_item for item in original_list]
"""

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = []
r = [i for i in t if i % 2 == 0]
print(r)


r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = []
print(r)


r = [i * j for i in t for j in t2]
print(r)


r = [1]
print(r)

r += [i for i in range(5)]
print(r)