import pandas as pd


class combineExelSheetsToOneSheet:
    def __init__(self, data_path, file_list, output_file_name):
        self.data_path = data_path
        self.file_list = file_list
        self.output_file_name = output_file_name

    def combine(self):
        df_list = []

        for file in self.file_list:
            df_list.append(
                pd.read_excel(self.data_path + file, engine="openpyxl", index_col=0)
            )

        df = pd.concat(df_list, axis=1)
        print(df)
        df.to_excel(self.output_file_name)


if __name__ == "__main__":
    file_list = ["csv_type1_1.xlsx", "csv_type1_2.xlsx"]
    comb = combineExelSheetsToOneSheet("../data/", file_list, "output.xlsx")
    comb.combine()