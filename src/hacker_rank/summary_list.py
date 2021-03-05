""" list """


l1 = ["A", "B", "C", "B"]

# listを検索
print("B" in l1)  # True

# listのindexを検索
print(l1.index("B"))  # True

# ある要素がlistに幾つ含まれるかを検索
print(l1.count("B"))  # 2


"""　2次元配列 """

l2 = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

# 2番目の要素でソートする

l2_sorted = sorted(l2, key=lambda x: x[2])
print(l2_sorted)


""" 内包表記 comprehension """

l3 = [x for x in range(5)]
print(l3)

l4 = [[x, y] for x in range(2) for y in range(3)]
print(l4)

l4 = [[x, y] for x in range(2) for y in range(3) if y == 2]
print(l4)

l5 = [
    [x, y, z] for x in range(2) for y in range(2) for z in range(2) if (x + y + z != 1)
]
print(l5)


""" swap """
l6 = [1, 2, 3, 4]
l6[1], l6[2] = l6[2], l6[1]
print(l6)


""" count """
l7 = [1, 2, 3, 1, 1]

print(l7.count(1))  # 3
