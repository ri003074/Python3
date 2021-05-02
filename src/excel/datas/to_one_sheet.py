import win32com.client
import os
import glob

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Add()

files = glob.glob("*.csv")
print(files)
print(wb.Sheets.Count)
for file in files:
    wb2 = xl.Workbooks.Open(Filename=os.getcwd() + "/" + file)
    wb2.Sheets(1).Copy(After=wb.Sheets(wb.Sheets.Count))
