import win32com.client
import os
import glob

xlLegendPositionBottom = -4107
xlLineMarkers = 65

xl = win32com.client.Dispatch("Excel.Application")


def get_last_row():
    return ws.Cells(ws.Rows.Count, 1).End(-4162).Row


def get_last_column():
    return ws.Cells(1, ws.Columns.Count).End(-4159).Column


xl.Visible = True

files = glob.glob("./datas/*.csv")
for file in files:
    wb = xl.Workbooks.Open(Filename=os.getcwd() + file)

    ws = wb.ActiveSheet

    chart = ws.Shapes.AddChart2().Chart
    chart.ChartType = xlLineMarkers
    chart.SetSourceData(
        ws.Application.Range(
            ws.Cells(1, 1), ws.Cells(get_last_row(), get_last_column())
        )
    )
    chart.ChartTitle.Text = ws.Cells(1, 1)
    chart.HasLegend = True
    chart.Legend.Position = xlLegendPositionBottom

    title = ws.Cells(1, 1)
    ws.Shapes(1).Chart.Export(Filename=os.getcwd() + "/datas/" + str(title) + ".png")
    wb.Close()
