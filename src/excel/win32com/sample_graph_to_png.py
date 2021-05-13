import win32com.client
import os
import time
import glob

# input_file = "202105120920_hei10_site1_free_meas"
# save_dir = "/" + input_file + "/"
# os.makedirs(input_file, exist_ok=True)

# xl = win32com.client.Dispatch("Excel.Application")
# xl.Visible = True

# wb = xl.Workbooks.Open(os.getcwd() + "/" + input_file + ".xlsx")
# ws = wb.Sheets(1)

# for i in range(ws.Shapes.Count):
#     title = ws.Shapes(i + 1).Chart.ChartTitle.Text
#     ws.Shapes(i + 1).Select()
#     # time.sleep(1)
#     ws.Shapes(i + 1).Chart.Export(Filename=os.getcwd() + save_dir + title + ".png")

# wb.Close()


file_list = glob.glob(os.getcwd() + "/../openpyxl/dut*.xlsx")
print(file_list)

for file in file_list:
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True

    wb = xl.Workbooks.Open(file)
    ws = wb.Sheets(1)

    for i in range(ws.Shapes.Count):
        title = ws.Shapes(i + 1).Chart.ChartTitle.Text
        ws.Shapes(i + 1).Select()
        ws.Shapes(i + 1).Chart.Export(Filename=os.getcwd() + "/" + title + ".png")

    wb.Close()
    xl.Quit()
