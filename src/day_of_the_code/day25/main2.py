import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_sc_data_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sc_data_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sc_data_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_sc_data_count)

dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts": [gray_sc_data_count, cinnamon_sc_data_count, black_sc_data_count],
}

df = pandas.DataFrame(dic)
df.to_csv("new_fur_color.csv")
