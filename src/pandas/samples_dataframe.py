import pandas as pd

data = [
    ["p1", 3, 1, 2],
    ["p2", 90, 70, 75],
    ["p3", 2, 1, 3],
]

df = pd.DataFrame(data, columns=["pin", "test1", "test2", "test3"])
# df.to_csv("data.csv", encoding="shift-jis", index=False)
# df.to_excel("data.xlsx", encoding="shift-jis", index=False)

print(df)