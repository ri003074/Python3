import win32com.client

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Add()
ws = wb.Worksheets(1)
ws.Cells(1, 1).Value = 1
