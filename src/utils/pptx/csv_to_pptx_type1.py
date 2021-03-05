import csv
from collections import defaultdict

data_path = "./data/"


class PowerPoint:
    """expected csv format is following
    pin, test1, test2,,,
    p1, 1, 2,,
    p2, 3, 4,,
    p3, 5, 6,,
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = defaultdict(list)
        self.categories = []

    def make_data(self):
        tmp_data = []
        with open(self.input_file, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.categories.append(line[0])
                tmp_data.append(line[1:])

        for i in range(0, len(tmp_data[0])):
            for j in range(1, len(tmp_data)):
                self.data[tmp_data[0][i]].append(tmp_data[j][i])


pptx = PowerPoint(data_path + "csv_type1_1.csv", data_path + "csv_type1_1.pptx")
pptx.make_data()
print(pptx.categories[1:])
print(pptx.data)