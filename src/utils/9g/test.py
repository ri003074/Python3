abc = ["abc", "def", "ghi"]

dic = {"abc": "AAA", "def": "DDD"}


for i in range(len(abc)):
    for key, value in dic.items():
        if abc[i] == key:
            abc[i] = value

print(abc)

