import pandas as pd


class CombineExcelFiles:
    def __init__(self, data_path, file_list):
        self.file_list = file_list
        self.data_path = data_path

    def combine_excel_files(self):
        writer = pd.ExcelWriter("summary.xlsx", engine="xlsxwriter")
        for file in self.file_list:
            df = pd.read_excel(self.data_path + file, engine="openpyxl", index_col=0)
            df.to_excel(writer, index=True, sheet_name=file)
        writer.save()


if __name__ == "__main__":
    file_list = ["csv_type1_1.xlsx", "csv_type1_2.xlsx"]
    data_path = "../data/"
    combine = CombineExcelFiles(data_path, file_list)
    combine.combine_excel_files()
