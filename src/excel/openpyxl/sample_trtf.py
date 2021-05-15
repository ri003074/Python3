from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

pin_list = ["p1558", "p2222", "p3333", "p4444"]
dut1 = [["tr", "tf"], [57, 63], [59, 40], [50, 52], [56, 54]]
dut2 = [["tr", "tf"], [56, 62], [58, 39], [49, 51], [55, 53]]

datas = [dut1, dut2]
file_names = ["dut1", "dut2"]
for index, data in enumerate(datas):
    wb = Workbook()
    ws = wb.active
    for row_index in range(1, len(pin_list) + 1):
        ws.cell(row=row_index + 1, column=1).value = pin_list[row_index - 1]

    for row_index in range(len(data)):
        for column_index in range(1, len(data[0]) + 1):
            ws.cell(row=row_index + 1, column=column_index + 1).value = data[row_index][
                column_index - 1
            ]

    categories = Reference(ws, min_row=2, min_col=1, max_row=ws.max_row, max_col=2)
    values = Reference(
        ws, min_row=1, min_col=2, max_row=ws.max_row, max_col=ws.max_column
    )

    chart = LineChart()
    # chart.legend = None
    chart.legend.position = "b"
    chart.title = file_names[index]
    chart.height = 10
    chart.width = 20
    chart.add_data(values, titles_from_data=True)
    chart.set_categories(categories)
    chart.y_axis.title = "ps"
    chart.y_axis.scaling.max = 80
    chart.y_axis.scaling.min = 0

    for i in range(len(chart.series)):
        s1 = chart.series[i]
        s1.marker.symbol = "circle"
        s1.graphicalProperties.line.noFill = True
    ws.add_chart(chart, "B4")
    wb.save(file_names[index] + ".xlsx")
