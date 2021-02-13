import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference

df = pd.read_csv("csv_sample.csv")
df = df.loc[:, ~df.columns.str.match("Unnamed")]
df.to_excel("csv_sample.xlsx", index=False)


wb = load_workbook("csv_sample.xlsx")
ws = wb.active

values = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=4)
categories = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=4)
chart = LineChart()
chart.legend = None
chart.title = "Fruits"

chart.add_data(values, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "B4")
wb.save("output.xlsx")
