# -*- coding:utf-8 -*-
# import tkinter
# import tkinter.filedialog

from tkinter import Tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)


root = Tk()
root.title("dclog")
frame = MainFrame(root)
frame.mainloop()


# def file_read():

#     # ファイル選択ダイアログの表示
#     read_file_path = tkinter.filedialog.askopenfilename()
#     write_file_path = tkinter.filedialog.asksaveasfilename()

#     # ファイルが選択された場合
#     if len(read_file_path) != 0:
#         with open(write_file_path, "w") as fw:
#             with open(read_file_path, "r") as f:
#                 for line in f.read().splitlines():
#                     fw.write(line + "\n")


# class Application(tkinter.Tk):
#     def __init__(self):
#         super().__init__()

#         # アプリのタイトル
#         self.title("Dc log to graph")

#         # 読み込みボタンの作成と配置
#         self.read_button = tkinter.Button(
#             self,
#             text="ファイル読み込み",
#             command=self.read_button_func,
#             # background="black",
#         )
#         self.read_button.pack()

#     def read_button_func(self):
#         "読み込みボタンが押された時の処理"

#         # ファイルを読み込み
#         file_read()

#         # 読み込んだ結果を画面に描画
#         # self.text_canvas.create_text(300, 200, text=data)


# # GUIアプリ生成
# app = Application()
# app.mainloop()
