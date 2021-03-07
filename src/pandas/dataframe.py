import pandas
from collections import defaultdict

df = pandas.read_csv("./data/csv_type1_1.csv")
arr = df["test1"].values.tolist()
print(arr)

arr2 = defaultdict(list)
for col in df.columns:
    print(col)
    arr2[col] = df[col].values.tolist()

print(arr2)
