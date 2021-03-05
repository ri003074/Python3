""" 辞書 dictionary """

d1 = {"a": 1, "b": 2}

d1["c"] = 3
print(d1)

for key, value in d1.items():
    print(key)
    print(value)


d2 = {"c": 1, "b": 3, "a": 2}

d2_key_sort = sorted(d2.items())
print(d2_key_sort)

d2_value_sort = sorted(d2.items(), key=lambda x: x[1])
print(d2_value_sort)


""" comprehension """

a1 = ["a", "b", "c"]

d3 = {k: i for i, k in enumerate(a1)}
print(d3)
