import win32com.client
import numpy as np
import time
import sys


arr = [
    ["a", "b", "c"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

arr = np.arange(100).reshape(10, 10)
tbl_rows = len(arr)
tbl_columns = len(arr[0])


pptx = win32com.client.GetActiveObject("PowerPoint.Application")
active_presentation = pptx.ActivePresentation
slide_width = active_presentation.PageSetup.SlideWidth
slide_height = active_presentation.PageSetup.SlideHeight

sld = active_presentation.Slides.Add(Index=1, Layout=4)
sld.Select()

print(slide_width)
# sys.exit()

tbl = sld.Shapes.AddTable(tbl_rows, tbl_columns).Table

start = time.time()
for i in range(tbl_rows):
    # tbl.Rows(i + 1).Height = slide_height / tbl_rows
    tbl.Rows(i + 1).Height = 9
    for j in range(tbl_columns):
        # tbl.Columns(j + 1).Width = slide_width / tbl_columns
        tbl.Columns(j + 1).Width = 54
        tbl.Cell(i + 1, j + 1).Shape.TextFrame.TextRange.Text = arr[i][j]

# for i in range(1, tbl.Columns.Count + 1):
#     tbl.Columns(i).Width = 72

# for i in range(1, tbl.Rows.Count + 1):
#     tbl.Rows(i).Height = 18

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
shp = sld.Shapes(2)
shp.Left = slide_width / 2 - shp.width / 2
shp.Top = slide_height * 1 / 4
