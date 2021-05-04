import pandas as pd

# data = [
#     ["p1", 3, 1, 2],
#     ["p2", 90, 70, 75],
#     ["p3", 2, 1, 3],
# ]

# df = pd.DataFrame(data, columns=["pin", "test1", "test2", "test3"])
# # df.to_csv("data.csv", encoding="shift-jis", index=False)
# # df.to_excel("data.xlsx", encoding="shift-jis", index=False)

# df["avg"] = df.mean(axis="columns")
# df["min"] = df.min(axis="columns")
# df["max"] = df.max(axis="columns")
# print(df)


csv_type2_1 = [[1, "p1", 1], [1, "p2", 4], [2, "p3", 3], [2, "p4", 5]]

df = pd.DataFrame(csv_type2_1, columns=["test", "pin", "data"])

for index, group in df.groupby("test"):
    print(group)
