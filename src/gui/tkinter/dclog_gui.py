# -*- coding:utf-8 -*-
import tkinter
import tkinter.filedialog


def file_read():

    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename()

    row_no = 0
    data = []
    # ファイルが選択された場合
    if len(file_path) != 0:

        # ファイルを開いて読み込んでdataに格納
        with open(file_path, "r") as f:
            for line in f.read().splitlines():
                data.append(str(row_no) + "," + line)

    # ファイル選択がキャンセルされた場合

    print(data)
    return data


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # アプリのタイトル
        self.title("Dc log to graph")

        # テキスト表示キャンバスの作成と配置
        self.text_canvas = tkinter.Canvas(self, width=600, height=400, bg="#D0D0D0")
        self.text_canvas.pack()

        # 読み込みボタンの作成と配置
        self.read_button = tkinter.Button(
            self,
            text="ファイル読み込み",
            command=self.read_button_func,
            background="black",
        )
        self.read_button.pack()

        self.condition_buttion = tkinter.Button(self, text="Simple CSV")
        self.condition_buttion.pack()

    def read_button_func(self):
        "読み込みボタンが押された時の処理"

        # ファイルを読み込み
        data = file_read()

        # 読み込んだ結果を画面に描画
        self.text_canvas.create_text(300, 200, text=data)


# GUIアプリ生成
app = Application()
app.mainloop()
