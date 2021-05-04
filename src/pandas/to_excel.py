import pandas as pd

df1 = pd.DataFrame(
    [["a", "b"], ["c", "d"]], index=["row1", "row2"], columns=["col1", "col2"]
)
df2 = pd.DataFrame(
    [["c", "d"], ["e", "f"]], index=["row1", "row2"], columns=["col1", "col2"]
)

with pd.ExcelWriter("data.xlsx") as writer:
    df1.to_excel(writer, sheet_name="df1")
    df2.to_excel(writer, sheet_name="df2")

df3 = pd.read_csv("data.csv")
df4 = pd.read_excel("data.xlsx")
print(df3)
print(df4)
