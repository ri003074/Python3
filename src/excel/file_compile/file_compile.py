import glob
import pandas as pd
import numpy as np


files = glob.glob("data*.xlsx")
print(files)

lst = []

for file in files:
    lst.append(pd.read_excel(file, engine="openpyxl"))

df = pd.concat(lst)
df.to_excel("total.xlsx", index=False)


writer = pd.ExcelWriter("total3.xlsx", engine="xlsxwriter")
data_list = []
for index, file in enumerate(files):
    df = pd.read_excel(file, engine="openpyxl", index_col=0)
    print(df)
    df.to_excel(writer, index=True, sheet_name=file)
    data_list.append(df)

# writer.close()


df1 = pd.read_excel("data2.xlsx", engine="openpyxl", index_col=0)
df2 = pd.read_excel("data1.xlsx", engine="openpyxl", index_col=0)


print(df1.columns)
print(df1.index)
print(df1["test1"].to_list())
print(df1["test1"].to_list() + df2["test1"].to_list())
print(df1["test2"].to_list() + df2["test2"].to_list())

data = {
    "test1": np.array(df1["test1"]) - np.array(df2["test1"]),
    "test2": np.array(df1["test2"]) - np.array(df2["test2"]),
}

df3 = pd.DataFrame(data=data, index=df1.index, columns=df1.columns)
print(df3)

df3.to_excel(writer, index=True, sheet_name="summary")

df4 = df1 - df2
df4.to_excel(writer, index=True, sheet_name="summary2")

writer.save()