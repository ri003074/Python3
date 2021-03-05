from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.util import Pt

categories = [
    "p1",
    "p2",
    "p3",
    "p4",
    "p5",
    "p6",
    "p7",
    "p8",
    "p9",
    "p10",
    "p11",
    "p12",
    "p13",
    "p14",
    "p15",
    "p16",
    "p17",
    "p18",
    "p19",
    "p20",
]

test_infos = [
    {
        "test": "test1",
        "data": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    },
    {
        "test": "test2",
        "data": (
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
        ),
    },
]

# create presentation with 1 slide ------
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide_width = prs.slide_width
slide_height = prs.slide_height
print(slide_width)
print(slide_height)
print(Inches(10))
print(Inches(7.5))

# define chart data ---------------------
chart_data = ChartData()
chart_data.categories = categories

for test_info in test_infos:
    chart_data.add_series(test_info["test"], test_info["data"])

# chart size
chart_width = Inches(8)
chart_height = Inches(4)

# chart position
chart_x = (slide_width - chart_width) / 2
chart_y = (slide_height - chart_height) / 2

# add chart to slide --------------------
x, y, cx, cy = chart_x, chart_y, chart_width, chart_height
chart = slide.shapes.add_chart(XL_CHART_TYPE.LINE, x, y, cx, cy, chart_data).chart

# グラフレジェンド
chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM

# グラフタイトル
chart.has_title = True
chart.chart_title.has_text_frame = True
chart.chart_title.text_frame.text = "abc"
chart.chart_title.text_frame.paragraphs[0].font.size = Pt(12)

value_axis = chart.value_axis
value_axis.maximum_scale = 100
value_axis.minimum_scale = 0
value_axis.has_title = True
value_axis.axis_title.has_text_frame = True
value_axis.axis_title.text_frame.text = "mV"
value_axis.axis_title.text_frame.paragraphs[0].font.size = Pt(10)
value_axis.major_unit = 20
tick_labels = value_axis.tick_labels
# tick_labels.number_format = "mV"
tick_labels.font.bold = True
tick_labels.font.size = Pt(14)

prs.save("chart-02.pptx")
