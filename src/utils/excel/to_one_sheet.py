import pandas as pd
import glob

files = glob.glob("*.csv")

with pd.ExcelWriter("data.xlsx") as writer:
    for file in files:
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name=file, index=False)
