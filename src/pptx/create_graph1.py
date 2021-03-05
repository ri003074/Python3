from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.util import Pt

# create presentation with 1 slide ------
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])

# define chart data ---------------------
chart_data = ChartData()
chart_data.categories = ["East", "West", "Midwest"]
chart_data.add_series("Series 1", (19.2, 21.4, 16.7))

# add chart to slide --------------------
x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data)


slide = prs.slides.add_slide(prs.slide_layouts[5])
# define chart data ---------------------
chart_data = ChartData()
chart_data.categories = ["East", "West", "Midwest"]
chart_data.add_series("Series 1", (19.2, 21.4, 16.7))
chart_data.add_series("Series 2", (17.2, 28.4, 13.7))

# add chart to slide --------------------
x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
chart = slide.shapes.add_chart(XL_CHART_TYPE.LINE, x, y, cx, cy, chart_data).chart
chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM

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

prs.save("chart-01.pptx")
