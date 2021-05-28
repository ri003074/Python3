import csv
import datetime
import matplotlib.pyplot as plt
import os
import pandas as pd
import win32com.client
from collections import OrderedDict
from glob import glob
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference

# import sys

now = datetime.datetime.now()
date_now = now.strftime("%Y%m%d%H%M")


class WaveData:
    def __init__(
        self, filename, folderpath, header=[], groupby="",
    ):
        self.file_name = filename
        self.folder_path = folderpath
        self.input_file = self.folder_path + self.file_name
        self.data_df = ""
        self.data_list = ""
        self.header = header
        self.groupby = groupby

    def make_df_and_xlsx(self):
        with open(self.input_file, mode="r", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            data = []

            for rows in reader:
                dic = OrderedDict()
                dic["condition"] = rows[0]
                for i in range(1, len(rows) - 1, 2):
                    try:
                        dic[rows[i].replace(" ", "")] = float(
                            rows[i + 1].replace(" ", "")
                        )
                    except ValueError:
                        dic[rows[i].replace(" ", "")] = rows[i + 1].replace(" ", "")

                data.append(dic)

            tmp_df = pd.DataFrame(data)  # tmp_df has "condition" columns
            self.data_df = tmp_df
            self.adjust_unit()  # adjust unit of dataframe

            if self.header:
                self.data_df = self.data_df.set_axis(self.header, axis="columns")
                self.data_df = self.data_df.set_index(self.header[0])
            else:
                self.data_df = tmp_df.set_index("condition")

            self.data_list = self.data_df.reset_index().values.tolist()

            if self.header:
                self.data_list.insert(0, self.header)
            else:
                self.data_list.insert(0, tmp_df.columns)

            # self.data_df.to_excel(self.input_file.replace("csv", "xlsx"))
            with pd.ExcelWriter(self.input_file.replace("csv", "xlsx")) as writer:
                self.data_df.to_excel(writer, sheet_name="summary")

                if self.groupby:
                    for name, group in self.data_df.groupby(self.groupby):
                        group.to_excel(writer, sheet_name=name)

    def make_excel_graph(
        self,
        data_start_column,
        data_end_column,
        chart_yaxis_title="",
        chart_yaxis_scaling_min="",
        chart_yaxis_scaling_max="",
        chart_yaxis_major_unit="",
        chart_position="E5",
        chart_height=9,
        chart_width=16,
    ):
        wb = load_workbook(self.input_file.replace("csv", "xlsx"))
        for i in range(len(wb.worksheets)):
            ws = wb.worksheets[i]

            values = Reference(
                ws,
                min_row=1,
                min_col=data_start_column,
                max_row=ws.max_row,
                max_col=data_end_column,
            )
            categories = Reference(
                ws, min_row=2, min_col=1, max_row=ws.max_row, max_col=1
            )

            self.setup_excel_chart(
                values,
                categories,
                chart_height,
                chart_width,
                chart_yaxis_titles=chart_yaxis_title,
                chart_yaxis_scaling_mins=chart_yaxis_scaling_min,
                chart_yaxis_scaling_maxes=chart_yaxis_scaling_max,
                chart_yaxis_major_unit=chart_yaxis_major_unit,
            )

            ws.add_chart(self.chart, chart_position)
        wb.save(self.input_file.replace("csv", "xlsx"))

    def make_excel_graphs(
        self,
        data_start_column,
        chart_yaxis_titles=[],
        chart_yaxis_scaling_mins=[],
        chart_yaxis_scaling_maxes=[],
        chart_yaxis_major_unit=[],
        chart_height=9,
        chart_width=16,
    ):
        wb = load_workbook(self.input_file.replace("csv", "xlsx"))
        for i in range(len(wb.worksheets)):
            ws = wb.worksheets[i]

            for i in range(ws.max_column + data_start_column * -1 + 1):
                values = Reference(
                    ws,
                    min_row=1,
                    min_col=data_start_column + i,
                    max_row=ws.max_row,
                    max_col=data_start_column + i,
                )
                categories = Reference(
                    ws, min_row=2, min_col=1, max_row=ws.max_row, max_col=1
                )
                self.setup_excel_chart(
                    values,
                    categories,
                    chart_height,
                    chart_width,
                    chart_yaxis_titles=chart_yaxis_titles[i],
                    chart_yaxis_scaling_mins=chart_yaxis_scaling_mins[i],
                    chart_yaxis_scaling_maxes=chart_yaxis_scaling_maxes[i],
                    chart_yaxis_major_unit=chart_yaxis_major_unit[i],
                )

                ws.add_chart(self.chart, "B" + str(5 + 20 * i))
        wb.save(self.input_file.replace("csv", "xlsx"))

    def setup_excel_chart(
        self,
        values,
        categories,
        chart_height,
        chart_width,
        chart_yaxis_titles,
        chart_yaxis_scaling_mins,
        chart_yaxis_scaling_maxes,
        chart_yaxis_major_unit,
    ):
        self.chart = LineChart()
        self.chart.add_data(values, titles_from_data=True)
        self.chart.set_categories(categories)
        self.chart.height = chart_height
        self.chart.width = chart_width
        # self.chart.x_axis.title = "abc"
        self.chart.y_axis.title = chart_yaxis_titles
        self.chart.y_axis.scaling.min = chart_yaxis_scaling_mins
        self.chart.y_axis.scaling.max = chart_yaxis_scaling_maxes
        self.chart.y_axis.majorUnit = chart_yaxis_major_unit
        # chart.y_axis.majorGridlines = None

        for i in range(len(self.chart.series)):
            series = self.chart.series[i]
            series.marker.symbol = "circle"
            # series.marker.size = 10
            series.graphicalProperties.line.noFill = True

    def make_graph(
        self,
        df_columns_list,
        ylim,
        fontsize=14,
        xlabel="",
        ylabel="",
        style=["bo", "yo", "ro", "go"],
        filename="",
        rotation=0,
        figsize=(16, 9),
    ):

        self.setup_fig_and_ax(figsize)

        self.ax.set_xticks(
            [i for i in range(self.data_df.shape[0])]
        )  # set number of label

        self.data_df[df_columns_list].plot(
            ax=self.ax, ylim=ylim, style=style, legend=True, fontsize=fontsize
        )

        self.adjust_graph_params(rotation, xlabel, ylabel, fontsize)

        plt.savefig(self.folder_path + filename + ".png")
        plt.close("all")

        if self.groupby:
            for name, group in self.data_df.groupby(self.groupby):
                self.setup_fig_and_ax(figsize)

                self.ax.set_xticks(
                    [i for i in range(group.shape[0])]
                )  # set number of label
                group[df_columns_list].plot(
                    ax=self.ax, ylim=ylim, style=style, legend=True, fontsize=fontsize
                )

                self.adjust_graph_params(rotation, xlabel, ylabel, fontsize)

                plt.savefig(self.folder_path + name + "_" + filename + ".png")
                plt.close("all")

    def adjust_graph_params(self, rotation, xlabel, ylabel, fontsize):
        plt.xticks(rotation=rotation)
        self.ax.set_ylabel(ylabel, fontsize=fontsize)
        self.ax.set_xlabel(xlabel, fontsize=fontsize)
        self.ax.legend(fontsize=fontsize)

    def setup_fig_and_ax(self, figsize):
        self.fig = plt.figure(figsize=figsize)  # create figure object
        self.ax = self.fig.add_subplot(1, 1, 1)  # create axes object
        self.ax.yaxis.set_major_formatter(plt.FormatStrFormatter("%.1f"))
        # self.fig.subplots_adjust(bottom=0.2)

    def add_table_to_pptx(self, new_presentation, title, cell_width):
        if new_presentation:
            pptx = win32com.client.Dispatch("PowerPoint.Application")
            pptx.Visible = True
            self.active_presentation = pptx.Presentations.Open(
                os.getcwd() + "/advtemplate_mini.pptx"
            )
        else:
            pptx = win32com.client.GetActiveObject("PowerPoint.Application")
            self.active_presentation = pptx.ActivePresentation

        slide_width = self.active_presentation.PageSetup.SlideWidth
        slide_height = self.active_presentation.PageSetup.SlideHeight
        slide_count = self.active_presentation.Slides.Count

        slide = self.active_presentation.Slides.Add(Index=slide_count + 1, Layout=4)
        slide.Select()
        slide.Shapes(1).TextFrame.TextRange.Text = title

        table_rows = len(self.data_list)
        table_columns = len(self.data_list[0])
        table = slide.Shapes.AddTable(table_rows, table_columns).Table

        for i in range(table_rows):
            for j in range(table_columns):
                tr = table.Cell(i + 1, j + 1).Shape.TextFrame.TextRange
                try:
                    tr.Text = f"{self.data_list[i][j]:.1f}"
                except ValueError:
                    tr.Text = self.data_list[i][j]

                tr.Font.Size = 14

        for i in range(1, table.Columns.Count + 1):
            table.Columns(i).Width = cell_width[i - 1]

        shape = slide.Shapes(2)
        shape.Left = slide_width / 2 - shape.width / 2
        shape.Top = slide_height / 6

    def save_pptx(self, file_name):
        self.active_presentation.SaveAs(
            FileName=os.getcwd() + "/" + str(date_now) + "_" + file_name
        )

    def mul3(self, x):
        return x * 1e3

    def mul12(self, x):
        return x * 1e12

    def mulm9(self, x):
        return x * 1e-9

    def adjust_unit(self):
        if "EHEIGHT" in self.data_df.columns:
            self.data_df["EHEIGHT"] = self.data_df["EHEIGHT"].apply(self.mul3)

        if "EWIDTH" in self.data_df.columns:
            self.data_df["EWIDTH"] = self.data_df["EWIDTH"].apply(self.mul12)

        if "RISETIME" in self.data_df.columns:
            self.data_df["RISETIME"] = self.data_df["RISETIME"].apply(self.mul12)

        if "FALLTIME" in self.data_df.columns:
            self.data_df["FALLTIME"] = self.data_df["FALLTIME"].apply(self.mul12)

        if "FREQUENCY" in self.data_df.columns:
            self.data_df["FREQUENCY"] = self.data_df["FREQUENCY"].apply(self.mulm9)

        if "VAMPLITUDE" in self.data_df.columns:
            self.data_df["VAMPLITUDE"] = self.data_df["VAMPLITUDE"].apply(self.mul3)

        if "VPP" in self.data_df.columns:
            self.data_df["VPP"] = self.data_df["VPP"].apply(self.mul3)

        if "VMAXIMUM" in self.data_df.columns:
            self.data_df["VMAXIMUM"] = self.data_df["VMAXIMUM"].apply(self.mul3)

        if "VMINIMUM" in self.data_df.columns:
            self.data_df["VMINIMUM"] = self.data_df["VMINIMUM"].apply(self.mul3)


CELL_WIDTH_BASE = 72

filepaths = glob("sample_log/*.csv")
print(filepaths)
filepath = filepaths[0]
# filepath2 = filepaths[2]

data_summarize_eye = WaveData(
    filename="test.csv",
    folderpath=os.getcwd() + "/sample_log/",
    header=["condition", "EHEIGHT(mV)", "EWIDTH(mV)"],
    groupby="condition",
)
data_summarize_eye.make_df_and_xlsx()
data_summarize_eye.make_graph(
    df_columns_list=["EHEIGHT(mV)"],
    ylim=[300, 400],
    filename="8g_eheight",
    ylabel="ps",
)
data_summarize_eye.make_graph(
    df_columns_list=["EWIDTH(mV)"], ylim=[0, 10], filename="8g_ewidth",
)
data_summarize_eye.make_graph(
    df_columns_list=["EWIDTH(mV)", "EHEIGHT(mV)"],
    ylim=[0, 500],
    filename="8g_ewidth_eheight",
)
data_summarize_eye.add_table_to_pptx(
    new_presentation=False,
    title="eye",
    cell_width=[
        CELL_WIDTH_BASE * 5,
        CELL_WIDTH_BASE * 2,
        CELL_WIDTH_BASE * 2,
        CELL_WIDTH_BASE * 2,
        CELL_WIDTH_BASE * 2,
    ],
)
data_summarize_eye.make_excel_graphs(
    data_start_column=2,
    chart_yaxis_titles=["ps", "mV"],
    chart_yaxis_scaling_mins=[300, 0],
    chart_yaxis_scaling_maxes=[400, 10],
    chart_yaxis_major_unit=[20, 2],
)
data_summarize_eye.make_excel_graph(
    data_start_column=2,
    data_end_column=3,
    chart_yaxis_title="ps",
    chart_yaxis_scaling_min=0,
    chart_yaxis_scaling_max=400,
    chart_yaxis_major_unit=50,
    chart_position="L5",
)
# data_summarize_eye = WaveData(filepath2)
# data_summarize_eye.make_dataframe()
# data_summarize_eye.make_list()
# data_summarize_eye.make_xlsx()
# data_summarize_eye.make_graph(
#     df_columns_list=["RISETIME"],
#     ylim=[40, 70],
#     path=os.getcwd() + "/sample_log/",
#     initial="8G_",
# )
# data_summarize_eye.make_graph(
#     df_columns_list=["FALLTIME"],
#     ylim=[40, 70],
#     path=os.getcwd() + "/sample_log/",
#     initial="8G_",
# )
# data_summarize_eye.make_graph(
#     df_columns_list=["FALLTIME", "RISETIME"],
#     ylim=[40, 70],
#     path=os.getcwd() + "/sample_log/",
#     initial="8G_",
# )
# data_summarize_eye.add_table_to_pptx(
#     new_presentation=False,
#     title="overview",
#     cell_width=[
#         CELL_WIDTH_BASE * 4,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#         CELL_WIDTH_BASE * 1.1,
#     ],
# )
# data_summarize_eye.save_pptx(file_name="test")