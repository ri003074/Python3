# import csv
import pandas

# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)


# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperature = []
#     for row in data:
#         print(row)
#         temperature.append(row[1])


data = pandas.read_csv("weather_data.csv")

print(data)
print(data[data.day == "Monday"])

# data_dic = data.to_dict()
# print(data)
# print(data_dic)

# temp = data["temp"]

# average = temp.mean()
# print(average)

# max = temp.max()
# print(max)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data.temp)
# print(data.condition)


data_dict = {"students": ["A", "B", "C"], "scores": [1, 2, 3]}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
