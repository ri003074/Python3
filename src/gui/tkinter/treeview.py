import tkinter as tk
import tkinter.ttk as ttk

base = tk.Tk()
base.title(u"Treeview Test")
base.geometry("400x300")

tree = ttk.Treeview(base)
# フォーム上の場所
tree.place(x=10, y=100)
# 列を３列作る
tree["column"] = (1, 2, 3)
tree["show"] = "headings"
# ヘッダーテキスト
tree.heading(1, text="ID")
tree.heading(2, text="名前")
tree.heading(3, text="年齢")
# 列の幅
tree.column(1, width=100)
tree.column(2, width=200)
tree.column(3, width=100)
# データ挿入
tree.insert("", "end", values=("1", "山田 太郎", "43"))
tree.insert("", "end", values=("2", "佐藤 隆", "53"))
tree.insert("", "end", values=("3", "渡辺 一郎", "38"))
# 設置
tree.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

base.mainloop()
