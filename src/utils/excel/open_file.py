# import win32com.client
# import os

# xl = win32com.client.Dispatch("Excel.Application")
# xl.Visible = True
# wb = xl.Workbooks.Add()
# ws = wb.Sheets(1)
# data = [
#     ["title", "test1", "test2", "test3", "test4"],
#     ["p1", 1, 2, 3, 4],
#     ["p2", 4, 5, 6, 7],
#     ["p3", 7, 8, 9, 11],
# ]

# ws.Range(ws.Cells(1, 1), ws.Cells(len(data), len(data[0]))).Value = data
# xl.DisplayAlerts = False
# # wb.SaveAs(Filename=os.getcwd() + "/saved.csv", FileFormat=xlCSV)  # csv
# wb.SaveAs(Filename=os.getcwd() + "/data.xlsx")
# wb.SaveAs(Filename=os.getcwd() + "/data.csv", FileFormat=6)
# wb.Close()


import win32com.client
import os

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Open(os.getcwd() + "/data.csv")
ws = wb.ActiveSheet
ws.Cells(10, 10).Value = 2
wb.SaveAs(Filename=os.getcwd() + "/data.xlsx", FileFormat=51)
wb.Close()
