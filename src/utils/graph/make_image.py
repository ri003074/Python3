import pandas
import matplotlib.pyplot as plt
from collections import defaultdict


class Image:
    def __init__(self):
        self.markers = [".", "o", "^", "X", "D"]

    def make_graph(
        self,
        input_file,
        output_file,
        yaxis_min,
        yaxis_max,
        ytics,
        graph_title="",
        xlabel="",
        ylabel="",
    ):
        df = pandas.read_csv(input_file, index_col=[0])
        ax = df.plot(
            kind="line",
            figsize=(16, 9),
            title=graph_title,
            legend=True,
            ylim=[yaxis_min, yaxis_max],
            yticks=ytics,
            xticks=range(0, len(df.index)),
            fontsize=10,
            # marker="o",
        )
        ax.grid(axis="y")

        # ax.annotate("anontetion", xy=(2, 6))

        for i, line in enumerate(ax.get_lines()):
            line.set_marker(self.markers[i])
            ax.legend(ax.get_lines(), df.columns, loc="best", fontsize=20)

        ax.set_ylabel(ylabel, fontsize=20)
        ax.set_xlabel(xlabel)
        print(ax)
        fig = ax.get_figure()
        fig.savefig(output_file)


class ImageCreate:
    def __init__(self):
        self.markers = [".", "o", "^", "X", "D"]

    def make_graph(self, input_file, output_file, ylabel, yticks):
        df = pandas.read_csv(input_file)
        data = defaultdict(list)
        columns = []
        for col in df.columns:
            data[col] = df[col].values.tolist()
            columns.append(col)

        figure = plt.figure(
            figsize=(16, 9),
        )
        axes = figure.add_subplot(1, 1, 1)
        for i in range(1, len(columns)):
            axes.plot(
                data[columns[0]],
                data[columns[i]],
                label=columns[i],
                marker=self.markers[i - 1],
            )
        axes.legend(loc="upper right", fontsize=20)
        axes.grid(b=True, axis="y")
        axes.set_ylabel(ylabel, fontsize=20)
        plt.yticks(yticks)
        # plt.ylim([yaxis_min, yaxis_max])

        plt.savefig(output_file)


if __name__ == "__main__":
    data_path = "../data/"

    image = ImageCreate()
    image.make_graph(
        input_file=data_path + "csv_type1_1.csv",
        output_file="csv_type1_1.png",
        ylabel="mV",
        yticks=range(0, 20, 2),
        # yaxis_min=0,
        # yaxis_max=8,
    )
    image.make_graph(
        input_file=data_path + "csv_type1_2.csv",
        output_file="csv_type1_2.png",
        ylabel="mV",
        yticks=range(0, 10, 2),
        # yaxis_min=0,
        # yaxis_max=8,
    )
    # image = Image()
    # image.make_graph(
    #     input_file=data_path + "csv_type1_1.csv",
    #     output_file="csv_type1_1.png",
    #     yaxis_min=0,
    #     yaxis_max=8,
    #     ylabel="mV",
    #     ytics=range(0, 10, 2),
    # )
    # image.make_graph(
    #     input_file=data_path + "csv_type1_2.csv",
    #     output_file="csv_type1_2.png",
    #     yaxis_min=0,
    #     yaxis_max=10,
    #     ylabel="mV",
    #     ytics=range(0, 12, 2),
    # )
