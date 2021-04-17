import glob
import pandas as pd


files = glob.glob("data*.xlsx")
print(files)

lst = []

for file in files:
    lst.append(pd.read_excel(file, engine="openpyxl"))

df = pd.concat(lst)
df.to_excel("total.xlsx", index=False)


writer = pd.ExcelWriter("total3.xlsx", engine="xlsxwriter")
for index, file in enumerate(files):
    df = pd.read_excel(file, engine="openpyxl")
    df.to_excel(writer, index=False, sheet_name=file)

writer.save()
writer.close()