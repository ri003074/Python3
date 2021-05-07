# import win32com.client


# def activate_opend_excel():
#     xl = win32com.client.GetObject(Class="Excel.Application")
#     wb = xl.Workbooks(1)
#     ws = wb.Sheets(1)
#     print(wb.Name)
#     print(ws.Name)
#     ws.Range("A1:B2").Value = [[1, 2], [3, 4]]


# # activate_opend_excel()


# def write_value_to_cell():
#     xl = win32com.client.GetObject(Class="Excel.Application")
#     wb = xl.Workbooks(1)
#     ws = wb.Sheets(1)
#     ws.Cells.Clear()
#     data = [
#         ["title", "test1", "test2", "test3", "test4"],
#         ["p1", 1, 2, 3, 4],
#         ["p2", 4, 5, 6, 7],
#         ["p3", 7, 8, 9, 10],
#     ]

#     ws.Range(ws.Cells(1, 1), ws.Cells(len(data), len(data[0]))).Value = data


# write_value_to_cell()

import win32com.client
import os
xlCSV = 6

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Add()
ws = wb.Sheets(1)
data = [
    ["title", "test1", "test2", "test3", "test4"],
    ["p1", 1, 2, 3, 4],
    ["p2", 4, 5, 6, 7],
    ["p3", 7, 8, 9, 11],
]

ws.Range(ws.Cells(1, 1), ws.Cells(len(data), len(data[0]))).Value = data
xl.DisplayAlerts = False
# wb.SaveAs(Filename=os.getcwd() + "/saved.csv", FileFormat=xlCSV)  # csv
wb.SaveAs(Filename=os.getcwd() + "/saved.xlsx")
wb.Close()
