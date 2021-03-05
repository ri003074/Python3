csv_list = []
with open("a.csv") as f:
    for line in f.read().splitlines():
        csv_list.append(line.split(","))

dic = {}
for i in range(len(csv_list[0])):

    dic[csv_list[0][i]] = []
    for j in range(1, len(csv_list)):
        dic[csv_list[0][i]].append(csv_list[j][i])

average_list = []
average_key = []
for key, value in dic.items():
    average_key.append(key)
    average = 0
    for i in range(len(value)):
        average += int(value[i])

    average_list.append(str(int(average / i)))


print(",".join(average_key))
print(",".join(average_list))
