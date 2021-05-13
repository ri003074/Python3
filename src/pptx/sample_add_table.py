from pptx import Presentation
from pptx.util import Pt

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

prs = Presentation()
sld0 = prs.slides.add_slide(prs.slide_layouts[5])
slide_width = prs.slide_width
slide_height = prs.slide_height
sld0.shapes[0].text = "insert table"

table_shape = sld0.shapes.add_table(
    len(data), len(data[0]), 0, 0, slide_width, slide_height
)
table = table_shape.table


for i in range(len(data)):
    table.rows[i].height = int(slide_height / len(data))
    for j in range(len(data[0])):
        table.cell(i, j).text = str(data[i][j])
        table.columns[j].width = int(slide_width / len(data[0]))


for cell in iter_cells(table):
    for paragraph in cell.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(7)

prs.save("sample.pptx")
