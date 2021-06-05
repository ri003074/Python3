from pptx import Presentation
from pptx.util import Pt
import time
import numpy as np
import sys
from pptx.enum.text import PP_ALIGN


# from pptx.util import Inches


def iter_cells(table):
    for row in table.rows:
        for cell in row.cells:
            yield cell


data = [
    ["a", "b", "c"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [13, 14, 15],
    [13, 14, 15],
    [13, 14, 15],
    [13, 14, 15],
    [16, 17, 18],
    [16, 17, 18],
    [16, 17, 99],
]

data = np.arange(100).reshape(10, 10)

prs = Presentation()
sld0 = prs.slides.add_slide(prs.slide_layouts[5])
slide_width = prs.slide_width
slide_height = prs.slide_height
sld0.shapes[0].text = "insert table"

print(slide_width)
print(Pt(960 / 1.33333333333333333))  # 960pixel

table_shape = sld0.shapes.add_table(
    len(data), len(data[0]), 0, 0, slide_width, slide_height,
)
table = table_shape.table


start = time.time()
for i in range(len(data)):
    # table.rows[i].height = int(slide_height / len(data) / 2)
    table.rows[i].height = Pt(9 / 1.3333333333333)
    for j in range(len(data[0])):
        table.cell(i, j).text = str(data[i][j])
        table.cell(i, j).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        # table.columns[j].width = int(slide_width / len(data[0]))
        # table.columns[j].width = Pt(54 / 1.3333333333333333)
        table.columns[j].width = Pt(54)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# for cell in iter_cells(table):
#     for paragraph in cell.text_frame.paragraphs:
#         for run in paragraph.runs:
#             run.font.size = Pt(7)

# sld0.shapes[1].width = slide_width / 2

table_shape.left = int(slide_width / 2 - table_shape.width / 2)
table_shape.top = int(slide_height * 1 / 4)
prs.save("abc.pptx")
