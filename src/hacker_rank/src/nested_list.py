students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.1],
    ["Akriti", 41],
    ["Harsh", 39],
]
# students = [
#     ["Harry", 37.21],
#     ["Berry", 37.21],
#     ["Tina", 37.1],
#     ["Akriti", 41],
# ]

test = [
    ["b", 2],
    ["a", 1],
    ["c", 3],
]
n = 5

# grade = sorted(list(set([i[1] for i in students])), reverse=True)
# second_lowest_grade = grade[-2]

# d = {}
# for i in range(n):
#     d[students[i][0]] = students[i][1]

# name = [name for name, value in d.items() if value == second_lowest_grade]
# print(sorted(name))


s = sorted(set([x[1] for x in students]))
for name in sorted(x[0] for x in students if x[1] == s[1]):
    print(name)


# a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
# s = sorted(set([x[1] for x in a]))
# for name in sorted(x[0] for x in a if x[1] == s[1]):
#     print(name)
