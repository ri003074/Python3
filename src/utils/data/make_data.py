import pandas as pd

csv_type1_1 = [["p1", 1, 2, 1], ["p2", 2, 3, 4], ["p3", 3, 3, 3], ["p4", 4, 3, 5]]
csv_type2_1 = [[1, "p1", 1], [1, "p2", 4], [2, "p3", 3], [2, "p4", 5]]

df = pd.DataFrame(csv_type1_1, columns=["pin", "test1", "test2", "test3"])
df.to_csv("csv_type1_1.csv", index=False)

df = pd.DataFrame(csv_type2_1, columns=["test", "pin", "data"])
df.to_csv("csv_type2_1.csv", index=False)
