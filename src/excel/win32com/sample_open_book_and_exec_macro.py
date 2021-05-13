import win32com.client
import os
import time

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Open(os.getcwd() + "/macro.xlsm")
time.sleep(3)
xl.Application.Run("macro.xlsm" + "!macro1()")
wb.Close(SaveChanges=False)
xl.Quit()
