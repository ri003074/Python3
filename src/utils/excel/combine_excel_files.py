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


class CalcExcelSheets:
    def __init__(self, data_path, file):
        self.data_path = data_path
        self.file = file
        self.all_sheets = pd.read_excel(
            self.data_path + self.file, sheet_name=None, index_col=0, engine="openpyxl"
        )

        self.all_sheets_name = []

        for sheet in self.all_sheets.keys():
            self.all_sheets_name.append(sheet)

    def calc_excel_sheets(self, sheet_names):
        writer = pd.ExcelWriter("calced_" + self.file, engine="xlsxwriter")
        df_final = self.all_sheets[sheet_names[0]]
        df_final.to_excel(writer, index=True, sheet_name=sheet_names[0])

        for i in range(1, len(sheet_names)):
            df = self.all_sheets[sheet_names[i]]
            df.to_excel(writer, index=True, sheet_name=sheet_names[i])
            df_final += df

        df_final.to_excel(writer, index=True, sheet_name="calced_" + self.file)
        writer.save()


if __name__ == "__main__":
    file_list = ["csv_type1_1.xlsx", "csv_type1_2.xlsx"]
    data_path = "../data/"
    combine = CombineExcelFiles(data_path, file_list)
    combine.combine_excel_files()

    calc = CalcExcelSheets("./", "summary.xlsx")
    # print(calc.all_sheets_name)
    calc.calc_excel_sheets(calc.all_sheets_name)
