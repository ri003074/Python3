from collections import defaultdict

words = ["apple", "orange", "banana", "alpha", "beta", "apple"]
arr = []
results = {}
num = 0
for word in words:
    arr.append(word)
    key = word[0]
    if key not in results:  # 1
        print(arr.count(word))
        results[key + "-" + str(num)] = []  # 2
    results[key + "-" + str(num)].append(word)  # 3

    num = num + 1


print(results)
print(arr)


d = {"x": 100, "y": 200}

print(d.items())

for k, v in d.items():
    print(k, ":", v)


# defaultdict

s = "adfskja;gjldsfajslkfs"
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)


d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)


d = defaultdict(dict)
d["TEST"]["pin1"] = 1
d["TEST"]["pin2"] = 2
d["TEST2"]["pin1"] = 3
d["TEST2"]["pin2"] = 4
print(d)

d = defaultdict(list)
d["TEST"].append(1)
d["TEST"].append(1)
d["TEST"].append(1)
print(d)

for key1, val1 in d.items():
    print(key1)
    # for key2, val2 in val1.items():
    #     print(key2)
    #     print(val2)


# 二次元配列から辞書
data = [["a", "b"], ["c", "d"]]
dic = dict(data)
print(data)
print(dic)


d = {"x": [1, 2], "y": [3, 4]}
for key, value in d.items():
    print(key)
    print(value)
