import pandas

data_path = "../data/"


class Image:
    def __init__(self):
        pass

    def make_graph(
        self, input_file, output_file, yaxis_min, yaxis_max, ytics, graph_title=""
    ):
        df = pandas.read_csv(input_file, index_col=[0])
        ax = df.plot(
            figsize=(10, 10),
            title=graph_title,
            legend=True,
            ylim=[yaxis_min, yaxis_max],
            yticks=ytics,
        )
        ax.set_ylabel("mV")
        # ax.set_xlabel("mV")
        fig = ax.get_figure()
        fig.savefig(output_file)


if __name__ == "__main__":

    image = Image()
    image.make_graph(
        input_file=data_path + "csv_type1_1.csv",
        output_file="csv_type1_1.png",
        yaxis_min=0,
        yaxis_max=10,
        ytics=range(0, 12, 2),
    )
    image.make_graph(
        input_file=data_path + "csv_type1_2.csv",
        output_file="csv_type1_2.png",
        yaxis_min=0,
        yaxis_max=20,
        ytics=range(0, 22, 2),
    )
