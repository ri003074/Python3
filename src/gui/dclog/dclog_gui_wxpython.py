import wx
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference


class MainFrame(wx.Frame):
    chart_title = "Dc Test Result"
    chart_height = 10
    chart_width = 20
    y_axis_title = "mv"
    y_axix_min_value = 0
    y_axix_max_value = 10
    input_file_path = ""
    output_file_path = ""
    data = []
    wb = Workbook()
    ws = wb.active
    ws.title = "dc test"

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.open_dialog()
        self.read_file()
        self.make_excel()
        self.make_graph()

    def open_dialog(self):
        filter = "*.csv;*.txt"
        dialog = wx.FileDialog(None, "select file", style=wx.FD_OPEN, wildcard=filter)
        dialog.ShowModal()
        self.input_file_path = dialog.GetPath()
        self.output_file_path = self.input_file_path.replace("txt", "xlsx").replace(
            "csv", "xlsx"
        )

    def read_file(self):
        with open(self.input_file_path, "r") as f:
            for line in f.read().splitlines():
                self.data.append(line.split(","))

    def make_excel(self):
        for row_index in range(len(self.data)):
            for column_index in range(len(self.data[row_index])):
                try:
                    self.ws.cell(
                        row=row_index + 1, column=column_index + 1
                    ).value = float(self.data[row_index][column_index])

                except ValueError:
                    self.ws.cell(
                        row=row_index + 1, column=column_index + 1
                    ).value = self.data[row_index][column_index]

    def make_graph(self):
        values = Reference(self.ws, min_col=2, min_row=1, max_col=3, max_row=4)
        categories = Reference(self.ws, min_col=1, min_row=2, max_col=1, max_row=4)

        chart = LineChart()
        chart.legend.position = "b"
        chart.y_axis.title = self.y_axis_title
        chart.y_axis.scaling.max = self.y_axix_max_value
        chart.y_axis.scaling.min = self.y_axix_min_value
        chart.title = self.chart_title
        chart.height = self.chart_height
        chart.width = self.chart_width
        chart.add_data(values, titles_from_data=True)
        chart.set_categories(categories)

        self.ws.add_chart(chart, "B4")
        self.wb.save(self.output_file_path)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    # frame.Show()
    # app.MainLoop()
    app.Destroy()
