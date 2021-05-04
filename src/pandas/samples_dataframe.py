# import pandas as pd

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


# csv_type2_1 = [[1, "p1", 1], [1, "p2", 4], [2, "p3", 3], [2, "p4", 5]]

# df = pd.DataFrame(csv_type2_1, columns=["test", "pin", "data"])

# for index, group in df.groupby("test"):
#     print(group)

import pandas as pd

data = [
    ["p1", 1],
    ["p2", 6],
    ["p3", 3],
    ["p4", 4],
]


df = pd.DataFrame(data, columns=["pin", "data"])
df_merge = pd.concat([df, df])
print(df_merge.reset_index(drop=True))

# df = pd.DataFrame(data, columns=["pin", "data"])
# df1 = df[::2].reset_index(drop=True)
# df2 = df[1::2].reset_index(drop=True)


# diff_pin = df1["pin"] + "-" + df2["pin"]
# diff_data = df1["data"] - df2["data"]

# df_merge = pd.concat([diff_pin, diff_data], axis=1)
# print(df_merge)
