import csv
import datetime
import os
import re
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import win32com.client

from collections import OrderedDict
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.layout import Layout, ManualLayout
from openpyxl.chart.shapes import GraphicalProperties

# from openpyxl.drawing.line import LineProperties


from glob import glob

image_count = 0

now = datetime.datetime.now()
date_now = now.strftime("%Y%m%d%H%M")


"""
TODO
image->picture

"""

"""docstring smaple. function simple explanation is written in this line.

    if function detail explanation is necessary, write to here.

    Args:
        param1 (int): The first parameter
        param2 (str): The second parameter

    Returns:
        bool: The return value. True for success, False otherwise

    https://google.github.io/styleguide/pyguide.html
"""


class WaveData:
    def __init__(
        self,
        file_name,
        folder_path,
        new_presentation,
        index="Pin_Rate",
        groupby=None,
        header=None,
    ):
        self.data_df = ""
        self.data_vix = []
        self.data_overshoot = []
        self.file_name = file_name
        self.folder_path = folder_path
        self.groupby = groupby
        self.header = header
        self.index = index
        self.input_file = self.folder_path + self.file_name

        if new_presentation:
            pptx = win32com.client.Dispatch("PowerPoint.Application")
            pptx.Visible = True
            self.active_presentation = pptx.Presentations.Open(
                os.getcwd() + "/advtemplate_mini.pptx"
            )
        else:
            pptx = win32com.client.GetActiveObject("PowerPoint.Application")
            self.active_presentation = pptx.ActivePresentation

        self.slide_width = self.active_presentation.PageSetup.SlideWidth
        self.slide_height = self.active_presentation.PageSetup.SlideHeight
        self.slide_count = self.active_presentation.Slides.Count
        self.make_df_and_xlsx()

    def make_df_and_xlsx(self):
        """Make pandas dataframe and xlsx data from csv file

        Args:
            None

        Returns:
            None

        """
        with open(self.input_file, mode="r", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            data = []

            for rows in reader:
                match = re.match(r"(P(\d*).*?)_.*?_(.*?_.*?_.*?)_(.*?)_", rows[0])
                if match:
                    rows.insert(0, "Condition")
                    rows.insert(2, "Pin")
                    rows.insert(3, match.group(1))
                    rows.insert(4, "Pkind")

                    pin_kind, pin_order = self.check_pin_kind(match.group(1))

                    rows.insert(5, pin_kind)
                    rows.insert(6, "Vi")
                    rows.insert(7, match.group(3).replace("00V", "V"))
                    rows.insert(8, "Rate")
                    rows.insert(
                        9, match.group(4).replace("Rate0r", "").replace("ns", "ps")
                    )
                    rows.insert(10, "Order")
                    rows.insert(11, pin_order)

                dic = OrderedDict()
                for i in range(0, len(rows) - 1, 2):
                    try:
                        dic[rows[i].replace(" ", "").capitalize()] = float(
                            rows[i + 1].replace(" ", "")
                        )
                    except ValueError:
                        dic[rows[i].replace(" ", "").capitalize()] = rows[
                            i + 1
                        ].replace(" ", "")
                    except AttributeError:
                        dic[rows[i].replace(" ", "").capitalize()] = rows[i + 1]

                data.append(dic)

            self.data_df = pd.DataFrame(data)

            self.data_df.insert(
                1, "Pin_Rate", self.data_df["Pin"] + "_" + self.data_df["Rate"]
            )
            self.data_df.insert(
                2, "Pin_Vi", self.data_df["Pin"] + "_" + self.data_df["Vi"]
            )
            self.data_df.insert(
                3, "Pkind_Vi", self.data_df["Pkind"] + "_" + self.data_df["Vi"]
            )

            # adjust unit of dataframe
            self.adjust_unit()

            if self.header:
                self.data_df = self.data_df.set_axis(self.header, axis="columns")

            self.data_df = self.data_df.set_index(self.index)

            with pd.ExcelWriter(self.input_file.replace("csv", "xlsx")) as writer:
                self.data_df.to_excel(writer, sheet_name="summary")

                if self.groupby:
                    for name, group in self.data_df.groupby(self.groupby):
                        group.to_excel(writer, sheet_name=name)

    def make_excel_graph(
        self,
        file_name,
        chart_yaxis_scaling,
        chart_height=9,
        chart_width=16,
        chart_position="C2",
        chart_yaxis_title=None,
    ):
        """make specified excel graph using xlsx data

            Args:
                file_name (str): input excel file name
                chart_yaxis_scaling (list): values for yaxis scale.
                chart_height (float): chart height.
                chart_width (float): chart width.
                chart_position (str): chart position at excel.
                chart_yaxis_title: chart yaxis title

            Returns:
                None

        """

        wb = load_workbook(file_name)
        for i in range(len(wb.worksheets)):
            ws = wb.worksheets[i]

            values = Reference(
                ws, min_row=1, min_col=2, max_row=ws.max_row, max_col=ws.max_column,
            )
            categories = Reference(
                ws, min_row=2, min_col=1, max_row=ws.max_row, max_col=1
            )

            self.setup_excel_chart(
                values=values,
                categories=categories,
                chart_height=chart_height,
                chart_width=chart_width,
                chart_yaxis_titles=chart_yaxis_title,
                chart_yaxis_scaling_mins=chart_yaxis_scaling[0],
                chart_yaxis_scaling_maxes=chart_yaxis_scaling[1],
                chart_yaxis_major_unit=chart_yaxis_scaling[2],
            )

            ws.add_chart(self.chart, chart_position)
        wb.save(file_name)

    def make_excel_graphs(
        self,
        chart_height=9,
        chart_width=16,
        chart_yaxis_titles=[],
        chart_yaxis_scaling_mins=[],
        chart_yaxis_scaling_maxes=[],
        chart_yaxis_major_unit=[],
        data_start_column=0,
    ):
        """make excel graphs using xlsx data"""

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
                    values=values,
                    categories=categories,
                    chart_height=chart_height,
                    chart_width=chart_width,
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
        """excel chart setup"""

        self.chart = LineChart()
        self.chart.add_data(values, titles_from_data=True)
        self.chart.title = ""
        self.chart.set_categories(categories)
        self.chart.height = chart_height
        self.chart.width = chart_width
        self.chart.y_axis.title = chart_yaxis_titles
        self.chart.y_axis.scaling.min = chart_yaxis_scaling_mins
        self.chart.y_axis.scaling.max = chart_yaxis_scaling_maxes
        self.chart.y_axis.majorUnit = chart_yaxis_major_unit
        self.chart.y_axis.numFmt = "0.0"
        self.chart.x_axis.tickLblPos = "low"
        self.chart.layout = Layout(
            ManualLayout(x=0.1, y=0.1, h=0.8, w=0.8, xMode="edge", yMode="edge")
        )
        # self.chart.legend.legendPos = "tr"
        self.chart.legend.layout = Layout(
            manualLayout=ManualLayout(yMode="edge", xMode="edge", x=0.75, y=0.13)
        )
        self.chart.legend.spPr = GraphicalProperties()
        self.chart.legend.spPr.solidFill = "FFFFFF"
        self.chart.legend.spPr.ln.solidFill = "E0E0E0"
        self.chart.legend.spPr.ln.w = 1 * 12700

        # chart.y_axis.majorGridlines = None

        for i in range(len(self.chart.series)):
            series = self.chart.series[i]
            series.marker.symbol = "circle"
            # series.marker.size = 10
            series.graphicalProperties.line.noFill = True

    def make_graph(
        self,
        df_columns_list,
        yticks,
        figsize=(10, 5.5),
        file_name="default",
        fontsize=14,
        format="%.1f",
        rotation=45,
        style=["o", "o", "o", "o"],
        axhline=None,
        legends=None,
        pkind=None,
        xlabel=None,
        ylabel=None,
    ):
        """make specified graph from dataframe using matplotlib
        Args:
            df_columns_list (list): dataframe columns list to make graph
            yticks (list): yticks
            figsize (list): figure size
            file_name (str): filename
            fontsize (int): font size
            format (str): axis format settin
            rotation (int): rotation
            style (list): marker style
            axline (int): yaxis line
            legends (list): legend
            pkind (str): pin kind
            xlabel (str): xlabel
            ylabel (str): ylabel

        Returns:
            None
        """
        global image_count

        # for excel graph
        os.makedirs(self.folder_path + "excel_graph_data", exist_ok=True)

        # if needs to separate result per pin kind
        if pkind:
            df = self.data_df[self.data_df["Pkind"] == pkind].copy()
        else:
            df = self.data_df.copy()

        if self.groupby:
            for name, group in df.groupby(self.groupby):
                df_plot = group[df_columns_list].dropna(how="all")

                num_of_index = len(df_plot.index)

                if num_of_index == 2:
                    xmargin = 0.5

                else:
                    xmargin = 0.1

                self.setup_fig_and_ax(
                    figsize, bottom=0.3, xmargin=xmargin, format=format
                )

                # set number of label
                self.ax.set_xticks([i for i in range(group.shape[0])])

                print(df_plot)
                df_plot.plot(
                    ax=self.ax,
                    ylim=yticks[:2],
                    style=style,
                    legend=True,
                    fontsize=fontsize,
                )

                self.adjust_graph_params(
                    group_name=name,
                    legends=legends,
                    rotation=rotation,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    yticks=yticks,
                    fontsize=fontsize,
                    axhline=axhline,
                    # num_of_index=num_of_index,
                    grid=True,
                )

                num = f"{image_count:03}_"

                # for excel graph
                excel_file_name = (
                    self.folder_path
                    + "/excel_graph_data/"
                    + num
                    + self.file_name.replace(".csv", "")
                    + "_"
                    + name
                    + "_"
                    + "_".join(df_columns_list)
                    + ".xlsx"
                )

                df_to_excel = df_plot.set_axis(legends, axis=1)
                df_to_excel.to_excel(excel_file_name)
                self.make_excel_graph(
                    file_name=excel_file_name,
                    chart_yaxis_scaling=yticks,
                    chart_yaxis_title=ylabel,
                )

                file_name_full = (
                    self.folder_path + num + name + "_" + file_name + ".png"
                )
                plt.savefig(file_name_full)
                plt.close("all")

                self.add_slide_to_pptx(
                    title=num + name + "_" + file_name,
                    slide_count=self.slide_count,
                    layout=11,
                )

                self.add_picture_to_pptx(file_name_full=file_name_full)

        else:
            self.setup_fig_and_ax(figsize, bottom=0.3)

            # set number of label
            self.ax.set_xticks([i for i in range(self.data_df.shape[0])])

            self.data_df[df_columns_list].plot(
                ax=self.ax, ylim=yticks[:2], style=style, legend=True, fontsize=fontsize
            )

            self.adjust_graph_params(
                rotation=rotation,
                xlabel=xlabel,
                ylabel=ylabel,
                fontsize=fontsize,
                yticks=yticks,
                axhline=axhline,
                # num_of_index=len(self.data_df.index),
                legends=legends,
            )

            num = f"{image_count:03}_"
            file_name_full = self.folder_path + num + file_name + ".png"
            plt.savefig(self.folder_path + num + file_name + ".png")
            plt.close("all")
            self.add_slide_to_pptx(
                title=num + file_name, slide_count=self.slide_count, layout=11,
            )

            self.add_picture_to_pptx(file_name_full=file_name_full)

    def make_overshoot_graph(self, file, figsize=(10, 5.5), item_name="Overshoot"):
        self.setup_fig_and_ax(figsize=figsize, xmargin=0.01)

        match_pin_file = re.match(r".*(P.*?)_.*(Vih.*)_Rate0r(.*ns).*", file)

        pin_name = match_pin_file.group(1)
        test_rate = match_pin_file.group(3)
        vi = match_pin_file.group(2).replace("00V", "V")

        self.wf_txt_data_to_csv(file)

        df = pd.read_csv(file.replace(".txt", ".csv"), header=None)
        df = df.set_axis(["t", pin_name], axis=1)  # TODO change name
        df = df.set_index("t")

        x = np.array(df.index.tolist())
        y = np.array(df[pin_name].tolist())
        self.ax.fill_between(x, y, 0.25, where=y > 0.25, color="C0", alpha=0.2)

        df.plot(ax=self.ax)

        # make data for table outpu
        self.data_overshoot.append(
            {"Vi": vi, "Pin": pin_name, "rate": test_rate, "overshoot(v-ns)": 0}
        )

        # self.adjust_graph_params(
        #     rotation=rotation,
        #     xlabel=xlabel,
        #     ylabel=ylabel,
        #     fontsize=fontsize,
        #     yticks=[],
        #     axhline="",
        #     num_of_index=[],
        #     legends=[positive_pin_name, negative_pin_name],
        # )
        num = f"{image_count:03}_"
        pkind = self.check_pin_kind(pin_name)
        file_name_full = (
            self.folder_path + num + pkind[0] + "_" + vi + "_" + item_name + ".png"
        )
        plt.savefig(file_name_full)
        plt.close("all")
        self.add_slide_to_pptx(
            title=num + pkind[0] + "_" + vi + "_" + item_name,
            slide_count=self.slide_count,
            layout=11,
        )
        self.add_picture_to_pptx(file_name_full=file_name_full)

    def make_vix_graph(
        self,
        item_name,
        nega_pin_file,
        posi_pin_file,
        description=False,
        fontsize=14,
        figsize=(10, 5.5),
        reference_level=0,
        rotation=0,
        xlabel=None,
        ylabel=None,
    ):
        """make vix graph from posi/nega wave data file using matplotlib
        Args:
            item_name (str): item name (Vix)
            nega_pin_file (str): csv nega pin file name
            posi_pin_file (str): csv posi pin file name
            description (bool): if put vix min/max ft description
            fontsize (int): fontsize
            figsize (list): figure size
            reference_level (float): reference level
            rotation (int): xlabel rotation value
            xlabel (str): xlabel
            ylabel (str): ylabel
        Returns:
            None
        """
        global image_count

        self.setup_fig_and_ax(figsize=figsize, xmargin=0.01)

        match_posi_pin = re.match(r".*(P.*?)_.*(Vih.*)_Rate0r(.*ns).*", posi_pin_file)
        match_nega_pin = re.match(r".*(P.*?)_.*(Vih.*)_Rate0r(.*ns).*", nega_pin_file)

        positive_pin_name = match_posi_pin.group(1)
        negative_pin_name = match_nega_pin.group(1)
        test_rate = match_posi_pin.group(3)
        vi = match_posi_pin.group(2).replace("00V", "V")

        self.wf_txt_data_to_csv(posi_pin_file)
        self.wf_txt_data_to_csv(nega_pin_file)

        df_posi = pd.read_csv(posi_pin_file.replace(".txt", ".csv"), header=None)
        df_nega = pd.read_csv(nega_pin_file.replace(".txt", ".csv"), header=None)

        df_posi = df_posi.set_axis(["t", "wck_t"], axis=1)
        df_nega = df_nega.set_axis(["t", "wck_c"], axis=1)

        df_posi = df_posi.set_index("t")
        df_nega = df_nega.set_index("t")

        df_posi_nega = pd.concat([df_posi, df_nega], axis=1)

        # make diff column
        df_posi_nega["f(t)"] = df_posi_nega["wck_t"] - df_posi_nega["wck_c"]
        df_posi_nega = df_posi_nega.iloc[
            int(len(df_posi_nega) * 0.23) : int(len(df_posi_nega) * 0.73), :
        ]

        # make dataframe df_vix. df_vix has 4 data which wck_t - wck_c is close to 0
        # close to 0 or 0 means cross point
        df_tmp = df_posi_nega.copy()
        df_vix = pd.DataFrame()
        for i in range(2):
            val = self.getNearestValue(df_tmp["f(t)"].values.tolist(), 0)
            min_row1 = df_tmp[df_tmp["f(t)"] == val]
            df_vix = pd.concat([df_vix, min_row1])
            df_tmp = df_tmp.drop(min_row1.index)

        # get average in case there is no cross point in data
        df_vix["(wck_t+wck_c)/2"] = (df_vix["wck_t"] + df_vix["wck_c"]) / 2

        df_vix = df_vix["(wck_t+wck_c)/2"]
        df_vix = df_vix.reset_index()
        df_vix_list = df_vix.values.tolist()

        # add x, y cordinates of differeential input cross point voltage to graph
        for df_vix_p in df_vix_list:
            x_position = df_vix_p[0]
            y_position = df_vix_p[1]

            if x_position < df_posi_nega.index[int(len(df_posi_nega) / 2)]:
                label = "Vix_WCK_FR"
                vix_wck_fr = y_position - reference_level
            else:
                label = "Vix_WCK_RF"
                vix_wck_rf = y_position - reference_level

            x_position_offset = 0.0005e-8
            y_position_offset = 0.05

            self.ax.text(
                x_position + x_position_offset,
                (y_position + reference_level) / 2,
                f"{label}={y_position-reference_level:.2f}mV",
                backgroundcolor="white",
                zorder=11,
                fontfamily="monospace",
            )
            self.ax.annotate(
                "",
                xy=[x_position, y_position],
                xytext=[x_position, reference_level],
                arrowprops=dict(arrowstyle="<->"),
                size=5,
            )

        # for Min(f(t)), Max(f(t))
        max_index = df_posi_nega["f(t)"].idxmax()
        min_index = df_posi_nega["f(t)"].idxmin()
        max_index_values = df_posi_nega.loc[max_index]
        min_index_values = df_posi_nega.loc[min_index]

        # Max(f(t))
        self.ax.annotate(
            "",
            xy=[max_index_values.name, max_index_values["wck_t"]],
            xytext=[max_index_values.name, max_index_values["wck_c"]],
            arrowprops=dict(arrowstyle="->"),
            zorder=10,
        )
        max_ft = max_index_values["wck_t"] - max_index_values["wck_c"]
        self.ax.text(
            max_index_values.name + x_position_offset,  # includes offset
            (max_index_values["wck_t"] + max_index_values["wck_c"]) / 2
            + y_position_offset,
            f"Max(f(t))={max_ft:.2f}mV",
            backgroundcolor="white",
            fontfamily="monospace",
        )

        # Min(f(t))
        self.ax.annotate(
            "",
            xy=[min_index_values.name, min_index_values["wck_t"]],
            xytext=[min_index_values.name, min_index_values["wck_c"]],
            arrowprops=dict(arrowstyle="->"),
            zorder=10,
        )
        min_ft = min_index_values["wck_t"] - min_index_values["wck_c"]
        self.ax.text(
            min_index_values.name + x_position_offset,  # includes offset
            (min_index_values["wck_t"] + min_index_values["wck_c"]) / 2
            + y_position_offset,
            f"Min(f(t))={min_ft:.2f}mV",
            backgroundcolor="white",
            fontfamily="monospace",
        )

        # Vix_WCK_Ratio Calculation result
        x_position_vix_ratio_result = 0.35
        vix_wck_ratio_fr_min_t = (vix_wck_rf / abs(max_ft)) * 100
        vix_wck_ratio_rf_max_t = (vix_wck_fr / abs(min_ft)) * 100
        self.ax.text(
            x_position_vix_ratio_result,
            -0.2,
            f"Vix_WCK_Ratio = Vix_WCK_FR/|Min(f(t))| = {vix_wck_fr:.2f}/|{min_ft:5.2f}| = {vix_wck_ratio_rf_max_t:4.1f}%",
            transform=self.ax.transAxes,
            fontfamily="monospace",
        )
        self.ax.text(
            x_position_vix_ratio_result,
            -0.25,
            f"Vix_WCK_Ratio = Vix_WCK_Rf/ Max(f(t))  = {vix_wck_rf:.2f}/ {max_ft:5.2f}  = {vix_wck_ratio_fr_min_t:4.1f}%",
            transform=self.ax.transAxes,
            fontfamily="monospace",
        )

        # make data for table outpu
        self.data_vix.append(
            {
                "Vi": vi,
                "Positive Pin": positive_pin_name,
                "Negative Pin": negative_pin_name,
                "rate": test_rate,
                "Vix_WCK_FR/|Min(f(t))| (%)": vix_wck_ratio_fr_min_t,
                "Vix_WCK_Rf/Max(f(t)) (%)": vix_wck_ratio_rf_max_t,
            }
        )

        # reference level line
        # TODO needs to clean up
        self.ax.hlines(
            y=reference_level,
            xmin=df_posi_nega.index[0],
            xmax=df_posi_nega.index[len(df_posi_nega) - 1],
            color="black",
            linestyle="dashed",
            zorder=10,
        )

        df_posi_nega = df_posi_nega.drop("f(t)", axis=1)
        df_posi_nega.plot(ax=self.ax)

        self.adjust_graph_params(
            rotation=rotation,
            xlabel=xlabel,
            ylabel=ylabel,
            fontsize=fontsize,
            yticks=[],
            axhline="",
            # num_of_index=[],
            legends=[positive_pin_name, negative_pin_name],
        )
        num = f"{image_count:03}_"
        pkind = self.check_pin_kind(positive_pin_name)
        file_name_full = (
            self.folder_path + num + pkind[0] + "_" + vi + "_" + item_name + ".png"
        )
        plt.savefig(file_name_full)
        plt.close("all")
        self.add_slide_to_pptx(
            title=num + pkind[0] + "_" + vi + "_" + item_name,
            slide_count=self.slide_count,
            layout=11,
        )
        self.add_picture_to_pptx(file_name_full=file_name_full)

        # insert Min(f(t)), Max(f(t)), Vix example pic from spec sheet
        if description:
            self.add_slide_to_pptx(
                title="Vix", slide_count=self.slide_count, layout=11,
            )
            self.add_picture_to_pptx(
                file_name_full=os.getcwd() + "/images/Vix.png",
                resize=True,
                count_image=False,
            )
            self.add_slide_to_pptx(
                title="Min(f(t)), Max(f(t))", slide_count=self.slide_count, layout=11,
            )
            self.add_picture_to_pptx(
                file_name_full=os.getcwd() + "/images/ft.png",
                resize=True,
                count_image=False,
            )

    def getNearestValue(self, list, num):
        """return nearest value of num from list

        Args:
            list (list): list of num
            num (int): num of value

        Returns:
            nearest value of num from list
        """
        idx = np.abs(np.asarray(list) - num).argmin()
        return list[idx]

    def setup_fig_and_ax(self, figsize=(16, 9), bottom=0.2, xmargin=0.1, format="%.1f"):
        """set up matploblib fix and ax object

        Args:
            figsize (tuple): fig size
            bottom (float): bottom margin
            xmargin (float): xmargin
            format (str): yaxis format setting

        Returns:
            None
        """
        self.fig = plt.figure(figsize=figsize)  # create figure object
        self.ax = self.fig.add_subplot(1, 1, 1, xmargin=xmargin)  # create axes object
        self.ax.yaxis.set_major_formatter(plt.FormatStrFormatter(format))
        self.fig.subplots_adjust(bottom=bottom)

    def adjust_graph_params(
        self,
        legends,
        yticks,
        fontsize=14,
        # num_of_index=0,
        rotation=0,
        group_name="",
        xlabel=None,
        ylabel=None,
        axhline=None,
        grid=False,
    ):
        """adjust graph parameters

        Args:
            legends (list): legend list
            yticks (list): yticks min, max, resolution
            fontsize (int): font size
            rotation (int): rotation
            group_name (str): group name
            xlabel (str): xlabel
            ylabel (str): ylabel
            axline (float): axhline
            grid (bool): grid

        Returns:
            None
        """
        plt.xticks(rotation=rotation)
        self.ax.set_ylabel(ylabel, fontsize=fontsize)
        self.ax.set_xlabel(xlabel, fontsize=fontsize)
        self.ax.legend(labels=legends, fontsize=fontsize, loc="upper right")

        # set grid
        if grid:
            self.ax.grid(axis="y", linestyle="-", color="black", linewidth=1, alpha=0.2)

        if yticks:
            self.ax.set_yticks(np.arange(yticks[0], yticks[1] + yticks[2], yticks[2]))

        # add limit line in case AT condition Vih/Vil=1V/0V
        match_at_condition = re.match(r".*Vih1r0V_Vil0r0V", group_name)
        if match_at_condition and axhline:
            self.ax.axhline(
                y=axhline,
                # xmin=0,
                # xmax=num_of_index - 1,
                # linestyle={"dashed"},
                color="gray",
            )

    def add_vix_table_to_pptx(self, title, items, cell_width, cell_height=20):
        """add vix table to pptx

            Args:
                title (str): slide title
                items (list): items for table
                cell_width (list): cell width
                cell_height (int): cell height

            Returns:
                None
        """
        vix_data_list_to_table_df = pd.DataFrame(self.data_vix)
        print(vix_data_list_to_table_df)
        self.add_slide_to_pptx(title=title, slide_count=self.slide_count, layout=4)
        self.add_table(
            df=vix_data_list_to_table_df,
            items=items,
            cell_width=cell_width,
            cell_height=cell_height,
            slide_width=self.slide_width,
            slide_height=self.slide_height,
            rename={},
        )

    def add_summary_table_to_pptx(
        self,
        title,
        cell_width,
        items,
        cell_height=20,
        groupby_table=None,
        rename=None,
        pkind=None,
        sort=None,
    ):
        """add summary table to pptx

        add slide, add table to pptx.

            Args:
                title (str): slide title
                cell_width (list): cell width
                items (list): items for table
                cell_height (int): cell height
                groupby_table (str): group name of table in case separate table by group
                rename (dict): specify header original and after name in case rename
                pkind (str): pin kind
                sort (bool): if sort data by one of data frame column, specify df column name.

            Returns:
                None
        """

        self.add_slide_to_pptx(title=title, slide_count=self.slide_count, layout=4)

        # if needs to separate result per pin kind
        if pkind:
            data_list_to_table_df = (
                self.data_df[self.data_df["Pkind"] == pkind].copy().reset_index()
            )
        else:
            data_list_to_table_df = self.data_df.reset_index()

        if sort:
            data_list_to_table_df = data_list_to_table_df.sort_values(sort)

        # data_list_to_table_df = self.data_df.reset_index()
        self.add_table(
            df=data_list_to_table_df,
            items=items,
            cell_width=cell_width,
            cell_height=cell_height,
            slide_width=self.slide_width,
            slide_height=self.slide_height,
            rename=rename,
        )

        if groupby_table:
            for name, group in data_list_to_table_df.groupby(groupby_table):
                slide_count = self.active_presentation.Slides.Count
                self.add_slide_to_pptx(title=name, slide_count=slide_count, layout=4)
                data_list_to_table_df = group.reset_index()
                self.add_table(
                    df=data_list_to_table_df,
                    items=items,
                    cell_width=cell_width,
                    cell_height=cell_height,
                    slide_width=self.slide_width,
                    slide_height=self.slide_height,
                    rename=rename,
                )

    def add_pictures_to_pptx(self, file_list):
        """add pictures to pptx

        Args:
            file_list (list): image list

        Returns:
            None
        """
        for file in file_list:
            title = file.replace("\\", "xyz").replace(".png", "")
            title = re.sub(".*xyz", "", title)

            self.add_slide_to_pptx(title=title, slide_count=self.slide_count, layout=11)
            self.add_picture_to_pptx(
                file_name_full=file, resize=True, count_image=False
            )

    def add_picture_to_pptx(self, file_name_full, resize=False, count_image=True):
        """add picture to pptx

        Args:
            file_name_full (str): file name full path
            resize (bool): set True if resize image
            count_image (bool): image counter

        Returns:
            None
        """
        global image_count
        image = self.active_presentation.Slides(self.slide_count).Shapes.AddPicture(
            FileName=file_name_full, LinkToFile=-1, SaveWithDocument=-1, Left=0, Top=0,
        )

        if resize:
            image.Height = 400

        image.Left = self.slide_width / 2 - image.Width / 2
        image.Top = self.slide_height / 2 - image.Height / 2

        if count_image:
            image_count += 1

    def add_slide_to_pptx(self, title, slide_count, layout):
        """add slide to pptx

        Args:
            title (str): slide title
            slide_count (int): slide count
            layout (int): slide layout

        Returns:
            None
        """
        self.slide = self.active_presentation.Slides.Add(
            Index=slide_count + 1, Layout=layout
        )
        self.slide.Select()
        self.slide.Shapes(1).TextFrame.TextRange.Text = title
        self.slide.Shapes(1).TextFrame.TextRange.Font.Size = 20
        self.slide_count += 1

    def add_table(
        self, df, items, cell_width, cell_height, slide_width, slide_height, rename,
    ):
        """add table to slide.

        Args:
            df (DataFrame): data to table. data type is pandas dataframe
            items (list): items to add table
            cell_width (list): cell width
            cell_height (int): cell height
            slide_width (int): slide width
            slide_height (int): slide height
            rename (dict): specify before/after name as dict like {"Frequency":"Freq(GHz)"} if rename table header.

        Returns:
            None
        """
        df = df.loc[:, items]
        print(df)
        df = df.dropna(how="all", axis=1)  # drop all nan column
        data_list_to_table = df.values.tolist()
        data_list_to_table.insert(0, df.columns.tolist())

        table_rows = len(data_list_to_table)
        table_columns = len(data_list_to_table[0])
        table = self.slide.Shapes.AddTable(table_rows, table_columns).Table

        for i in range(table_rows):
            for j in range(table_columns):
                tr = table.Cell(i + 1, j + 1).Shape.TextFrame.TextRange
                try:
                    if data_list_to_table[i][j] == 9.91e37:
                        data_list_to_table[i][j] = "aquisition failure"

                    elif str(data_list_to_table[i][j]) == "nan":
                        data_list_to_table[i][j] = "-"

                    tr.Text = f"{data_list_to_table[i][j]:.1f}"
                except ValueError:
                    if rename:
                        for key, value in rename.items():
                            if key == data_list_to_table[i][j]:
                                tr.Text = value
                                break
                            else:
                                tr.Text = data_list_to_table[i][j]
                    else:
                        tr.Text = data_list_to_table[i][j]

                tr.Font.Size = 10
                tr.ParagraphFormat.Alignment = 2  # centering

        for i in range(1, table.Columns.Count + 1):
            table.Columns(i).Width = cell_width[i - 1]

        for i in range(1, table.Rows.Count + 1):
            table.Rows(i).Height = cell_height

        # adjust table position
        shape = self.slide.Shapes(2)
        shape.Left = slide_width / 2 - shape.width / 2
        shape.Top = slide_height / 6

    def save_pptx(self, file_name, folder_name):
        """save pptx file
        Args:
            file_name (str): file name

        Returns:
            None
        """
        self.active_presentation.SaveAs(
            FileName=folder_name + str(date_now) + "_" + file_name
        )

    def wf_txt_data_to_csv(self, file):
        """create csv file from osc output text file

        Args:
            file (str): file name

        Returns:
            None
        """
        print(file)
        with open(file.replace(".txt", ".csv"), "w", encoding="utf-8") as fw:
            flg = 0
            with open(file, encoding="utf-8") as fr:
                for line in fr.read().splitlines():
                    match_data = re.match(r"Data", line)

                    if line != "":
                        if flg:
                            fw.write(line)
                            fw.write("\n")

                        if match_data:
                            flg = 1

    def check_pin_kind(self, pin_name):
        """check pin kind and return pin kind and order for sort

        Args:
            pin_name(str): pin name like P1857A1

        Returns:
            pin_kind, pin_order
            pin_kind: "IO", "WCK", "CK", "CA", "CS",
            pin_order: "IO"->1, "WCK"->2, "CK"->3, "CA"->4, "CS"->5
        """
        match_pin_name = re.match(r"P(\d*).*", pin_name)
        pin_num = int(match_pin_name.group(1))

        if pin_num < 1857:
            pin_kind = "IO"
            pin_order = 1
        elif pin_num >= 1857 and pin_num <= 1888:
            pin_kind = "WCK"
            pin_order = 2
        elif pin_num >= 1889 and pin_num <= 1890:
            pin_kind = "CK"
            pin_order = 3
        elif pin_num >= 1921 and pin_num <= 1933:
            pin_kind = "CA"
            pin_order = 4
        elif pin_num >= 1953 and pin_num <= 1959:
            pin_kind = "CS"
            pin_order = 5
        else:
            print("Pkind Error")
            sys.exit()

        return pin_kind, pin_order

    def mul3(self, x):
        return x * 1e3

    def mul12(self, x):
        return x * 1e12

    def mulm9(self, x):
        return x * 1e-9

    def adjust_unit(self):
        """

        Args:
            None

        Returns:
            None
        """
        if "Eheight" in self.data_df.columns:
            self.data_df["Eheight"] = self.data_df["Eheight"].apply(self.mul3)

        if "Ewidth" in self.data_df.columns:
            self.data_df["Ewidth"] = self.data_df["Ewidth"].apply(self.mul12)

        if "Risetime" in self.data_df.columns:
            self.data_df["Risetime"] = self.data_df["Risetime"].apply(self.mul12)

        if "Falltime" in self.data_df.columns:
            self.data_df["Falltime"] = self.data_df["Falltime"].apply(self.mul12)

        if "Frequency" in self.data_df.columns:
            self.data_df["Frequency"] = self.data_df["Frequency"].apply(self.mulm9)

        if "Vamplitude" in self.data_df.columns:
            self.data_df["Vamplitude"] = self.data_df["Vamplitude"].apply(self.mul3)

        if "Vpp" in self.data_df.columns:
            self.data_df["Vpp"] = self.data_df["Vpp"].apply(self.mul3)

        if "Vmaximum" in self.data_df.columns:
            self.data_df["Vmaximum"] = self.data_df["Vmaximum"].apply(self.mul3)

        if "Vminimum" in self.data_df.columns:
            self.data_df["Vminimum"] = self.data_df["Vminimum"].apply(self.mul3)

        if "Pwidth" in self.data_df.columns:
            self.data_df["Pwidth"] = self.data_df["Pwidth"].apply(self.mul12)

        if "Pp" in self.data_df.columns:
            self.data_df["Pp"] = self.data_df["Pp"].apply(self.mul12)


if __name__ == "__main__":

    CELL_WIDTH_BASE = 72
    DATA_START_COLUMNS = 10
    FOLDER_PATH = os.getcwd() + "/20210602_debug_8gpe/"
    PPTX_FILE_NAME = "8GPE_TEST.pptx"
    OVERVIEW_FILE_NAME = "result_overview.csv"
    EYE_FILE_NAME = "result_eye.csv"
    HISTOGRAM_FILE_NAME = "result_histogram.csv"
    OSC_IMAGE_LIST_OVERVIEW = glob(FOLDER_PATH + "/*overview/*.png")
    OSC_IMAGE_LIST_EYE = glob(FOLDER_PATH + "/*eye/*.png")
    OSC_IMAGE_LIST_HISTOGRAM = glob(FOLDER_PATH + "/*histogram/*.png")
    DATA_GROUP = "Pkind_Vi"
    DATA_INDEX = "Pin_Rate"
    PE = "8GPE_"
    FREQ_YTICKS = [3.0, 5.0, 0.25]
    DUTY_YTICKS = [40.0, 60.0, 2.5]
    TRTF_YTICKS = [30.0, 70.0, 5]
    EHEIGHT_YTICS = [300, 400, 20]
    EWIDTH_YTICKS = [60, 120, 10]
    PP_YTICKS = [00, 50, 10]

    wave_data_overview = WaveData(
        file_name=OVERVIEW_FILE_NAME,
        folder_path=FOLDER_PATH,
        groupby=DATA_GROUP,
        index=DATA_INDEX,
        new_presentation=True,
    )
    wave_data_overview.make_overshoot_graph(
        file=FOLDER_PATH
        + "20210602_101849_P111A1_overview/P111A1_overview_Vih0r500V_Vil0r000V_Vt0r000V_Rate0r286ns_Duty0r500.txt"
    )
    wave_data_overview.make_vix_graph(
        posi_pin_file="./sample_log/P1859A2_RZX_Vih0r916V_Vil0r000V_Rate0r362ns_Speed2r759GHz_TopBase_Meas.txt",
        nega_pin_file="./sample_log/P1860A2_RZX_Vih0r916V_Vil0r000V_Rate0r362ns_Speed2r759GHz_TopBase_Meas.txt",
        description=True,
        item_name=PE + "Vix",
        reference_level=0.2,
        ylabel="mV",
    )
    wave_data_overview.make_vix_graph(
        posi_pin_file="./sample_log/P1859A2_RZX_Vih0r916V_Vil0r000V_Rate0r362ns_Speed2r759GHz_TopBase_Meas.txt",
        nega_pin_file="./sample_log/P1860A2_RZX_Vih0r916V_Vil0r000V_Rate0r362ns_Speed2r759GHz_TopBase_Meas.txt",
        description=False,
        item_name=PE + "Vix",
        reference_level=0.229,
        ylabel="mV",
    )
    wave_data_overview.add_vix_table_to_pptx(
        title="Vix",
        items=[
            "Positive Pin",
            "Negative Pin",
            "Vi",
            "rate",
            "Vix_WCK_FR/|Min(f(t))| (%)",
            "Vix_WCK_Rf/Max(f(t)) (%)",
        ],
        cell_width=[
            CELL_WIDTH_BASE * 1.1,
            CELL_WIDTH_BASE * 1.1,
            CELL_WIDTH_BASE * 2.0,
            CELL_WIDTH_BASE * 1.1,
            CELL_WIDTH_BASE * 2.0,
            CELL_WIDTH_BASE * 2.0,
        ],
        cell_height=20,
    )
    wave_data_overview.make_graph(
        df_columns_list=["Frequency"],
        file_name=PE + "Frequency",
        format="%.2f",
        legends=["Freq(GHz)"],
        yticks=FREQ_YTICKS,
        ylabel="GHz",
        # pkind="IO",
    )
    wave_data_overview.make_graph(
        df_columns_list=["Dutycycle"],
        file_name=PE + "Duty",
        legends=["Duty(%)"],
        yticks=DUTY_YTICKS,
        ylabel="%",
    )
    wave_data_overview.make_graph(
        axhline=60,  # limit reference line
        df_columns_list=["Risetime", "Falltime"],
        file_name=PE + "Risetime_Falltime",
        legends=["Tr(ps)", "Tf(ps)"],
        yticks=TRTF_YTICKS,
        ylabel="ps",
    )
    wave_data_overview.add_summary_table_to_pptx(
        title="overview",
        cell_width=[
            CELL_WIDTH_BASE * 1.1,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
            CELL_WIDTH_BASE * 1.2,
        ],
        items=[
            "Pin",
            "Vi",
            "Rate",
            "Frequency",
            "Dutycycle",
            "Risetime",
            "Falltime",
            "Overshoot",
            "Preshoot",
            "Pwidth",
        ],
        groupby_table="Vi",
        rename={
            "Risetime": "Tr(ps)",
            "Frequency": "Freq(GHz)",
            "Dutycycle": "Duty(%)",
            "Falltime": "Tf(ps)",
            "Overshoot": "Overshoot(%)",
            "Preshoot": "Preshoot(%)",
            "Pwidth": "Pwidth(ps)",
            "nan": "-",
        },
        # sort="Order"
        # pkind="IO"
    )
    wave_data_eye = WaveData(
        file_name=EYE_FILE_NAME,
        folder_path=FOLDER_PATH,
        groupby=DATA_GROUP,
        index=DATA_INDEX,
        new_presentation=False,
    )
    wave_data_eye.make_graph(
        df_columns_list=["Eheight"],
        file_name=PE + "Eheight",
        legends=["Eye Height(mV)"],
        ylabel="mV",
        yticks=EHEIGHT_YTICS,
    )
    wave_data_eye.add_summary_table_to_pptx(
        title="eye",
        cell_width=[
            # CELL_WIDTH_BASE * 5,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
            CELL_WIDTH_BASE * 2,
        ],
        items=["Pin", "Vi", "Rate", "Eheight"],
        rename={"Eheight": "Eye Height(mV)"},
        groupby_table="Vi",
    )
    # wave_data_eye.make_excel_graphs(
    #     data_start_column=DATA_START_COLUMNS,
    #     chart_yaxis_titles=["ps", "mV"],
    #     chart_yaxis_scaling_mins=[300, 0],
    #     chart_yaxis_scaling_maxes=[400, 10],
    #     chart_yaxis_major_unit=[20, 2],
    # )
    wave_data_histogram = WaveData(
        file_name=HISTOGRAM_FILE_NAME,
        folder_path=FOLDER_PATH,
        groupby=DATA_GROUP,
        index=DATA_INDEX,
        new_presentation=False,
    )
    wave_data_histogram.make_graph(
        df_columns_list=["Pp"],
        file_name=PE + "Jitter",
        legends=["PP(ps)"],
        ylabel="ps",
        yticks=PP_YTICKS,
    )
    wave_data_histogram.add_pictures_to_pptx(file_list=OSC_IMAGE_LIST_OVERVIEW,)
    wave_data_histogram.add_pictures_to_pptx(file_list=OSC_IMAGE_LIST_EYE,)
    wave_data_histogram.add_pictures_to_pptx(file_list=OSC_IMAGE_LIST_HISTOGRAM,)
    wave_data_overview.save_pptx(file_name=PPTX_FILE_NAME, folder_name=FOLDER_PATH)
