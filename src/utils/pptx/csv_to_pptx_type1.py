import csv
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from collections import defaultdict
from pptx.util import Pt

data_path = "../data/"


class PowerPoint:
    """expected csv format is following
    pin, test1, test2,,,
    p1, 1, 2,,
    p2, 3, 4,,
    p3, 5, 6,,
    """

    def __init__(
        self,
        output_file,
    ):
        self.output_file = output_file
        self.data = defaultdict(list)
        self.categories = []
        self.slide_template = "sample_slide.pptx"
        self.presentation = Presentation(self.slide_template)

    def make_data(self, input_file):
        tmp_data = []
        self.categories = []
        self.data = defaultdict(list)
        with open(input_file, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.categories.append(line[0])
                tmp_data.append(line[1:])

        self.categories.pop(0)

        for i in range(0, len(tmp_data[0])):
            for j in range(1, len(tmp_data)):
                self.data[tmp_data[0][i]].append(tmp_data[j][i])

    def make_graph(
        self,
        axis_min,
        axis_max,
        axis_unit,
        graph_title="",
        axis_title="",
    ):
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[5])
        slide_width = self.presentation.slide_width
        slide_height = self.presentation.slide_height

        # define chart data ---------------------
        chart_data = ChartData()
        chart_data.categories = self.categories

        for key, value in self.data.items():
            chart_data.add_series(key, value)

        # chart size
        chart_width = Inches(8)
        chart_height = Inches(4)

        # chart position
        chart_x = (slide_width - chart_width) / 2
        chart_y = (slide_height - chart_height) / 2

        # add chart to slide --------------------
        x, y, cx, cy = chart_x, chart_y, chart_width, chart_height
        chart = slide.shapes.add_chart(
            XL_CHART_TYPE.LINE, x, y, cx, cy, chart_data
        ).chart

        # グラフレジェンド
        chart.has_legend = True
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM

        # グラフタイトル
        if graph_title:
            chart.has_title = True
            chart.chart_title.has_text_frame = True
            chart.chart_title.text_frame.text = graph_title
            chart.chart_title.text_frame.paragraphs[0].font.size = Pt(12)

        # グラフ X軸
        value_axis = chart.value_axis
        value_axis.minimum_scale = axis_min
        value_axis.maximum_scale = axis_max
        value_axis.major_unit = axis_unit

        # グラフ X軸 タイトル
        if axis_title:
            value_axis.has_title = True
            value_axis.axis_title.has_text_frame = True
            value_axis.axis_title.text_frame.text = axis_title
            value_axis.axis_title.text_frame.paragraphs[0].font.size = Pt(10)
            # tick_labels = value_axis.tick_labels
            # tick_labels.font.bold = True
            # tick_labels.font.size = Pt(14)
            # tick_labels.number_format = "mV"

        self.presentation.save(self.output_file)


if __name__ == "__main__":
    pptx = PowerPoint(
        output_file=data_path + "csv_type1_1.pptx",
        # graph_title="sample graph",
    )
    pptx.make_data(
        input_file=data_path + "csv_type1_1.csv",
    )
    pptx.make_graph(
        axis_min=0,
        axis_max=50,
        axis_unit=5,
        axis_title="mV",
    )
    pptx.make_data(
        input_file=data_path + "csv_type1_2.csv",
    )
    pptx.make_graph(
        axis_min=0,
        axis_max=30,
        axis_unit=10,
    )
