import pandas as pd
import numpy as np
from collections import defaultdict

df = pd.read_csv("./data/csv_type1_1.csv")
print(df)
df.to_excel("abc.xlsx", index=False)
arr = df["test1"].values.tolist()
print(arr)

arr2 = defaultdict(list)
for col in df.columns:
    print(col)
    arr2[col] = df[col].values.tolist()

print(arr2)


data = {
    "name": ["高橋", "鈴木", "田中", "松本"],
    "score": [80, 90, 70, 75],
    "number": [1, 2, 1, 3],
    "sex": ["m", "f", "f", "m"],
}

df = pd.DataFrame(data, columns=["name", "sex", "number", "score"])
print(df)
df["result"] = np.nan
print(df)


def multiple(x):
    return x.iloc[2] * x.iloc[3]


df["result"] = df.apply(multiple, axis=1)
print(df)


df["result2"] = df["result"] + 1
print(df)
