import win32com.client
import os

xlLegendPositionBottom = -4107
xlLineMarkers = 65
msoTrue = -1
msoFalse = 0

title = ["dc_test_result"]
tests = ["test1", "test2", "test3", "test4"]
pins = ["p1", "p2", "p3", "p4", "p5"]
data = [[i * j for i in range(len(tests))] for j in range(len(pins))]


xl = win32com.client.GetObject(Class="Excel.Application")
wb = xl.Workbooks("for_job.xlsm")
ws = wb.sheets("for_job")


def get_last_row():
    return ws.Cells(ws.Rows.Count, 1).End(-4162).Row


def get_last_column():
    return ws.Cells(1, ws.Columns.Count).End(-4159).Column


ws.Cells.Clear()  # initialize
ws.Application.Range(
    ws.Cells(2, 1), ws.Cells(len(pins) + 1, 1)
).value = xl.Application.WorksheetFunction.Transpose(pins)
ws.Application.Range(ws.Cells(1, 2), ws.Cells(1, len(tests) + 1)).value = tests
ws.Application.Range(ws.Cells(1, 1), ws.Cells(1, 1)).value = title[0]
ws.Range(ws.Cells(2, 2), ws.Cells(get_last_row(), get_last_column())).Value = data


for i in reversed(range(ws.ChartObjects().Count)):
    ws.ChartObjects(i + 1).Delete()

chart = ws.Shapes.AddChart2().Chart
chart.ChartType = xlLineMarkers
chart.SetSourceData(
    ws.Application.Range(ws.Cells(1, 1), ws.Cells(get_last_row(), get_last_column()))
)
chart.ChartTitle.Text = title[0]
chart.HasLegend = True
chart.Legend.Position = xlLegendPositionBottom

for i in range(chart.FullSeriesCollection().Count):
    chart.FullSeriesCollection(i + 1).Format.Line.Visible = msoFalse

x_axes = chart.Axes(2)
x_axes.MinimumScale = 0
x_axes.MaximumScale = 20
x_axes.HasTitle = True
x_axes.AxisTitle.Text = "mV"
x_axes.MajorUnit = 4
# x_axes.MinorUnit = 2 #?

ws.ChartObjects().Top = ws.Range("B10").Top
ws.ChartObjects().Left = ws.Range("B10").Left
ws.ChartObjects().Height = 200
ws.ChartObjects().Width = 400

for i in range(ws.Shapes.Count):
    ws.Shapes(i + 1).Chart.Export(Filename=os.getcwd() + "/" + title[0] + ".png")
