# import wx

# app = wx.App()

# frm = wx.Frame(None, title="hello")

# panel = wx.Panel(frm, -1)
# # text_ctrl1 = wx.StaticText(panel, -1, pos=(10, 10), size=(40, 10), label="Left")
# # text_ctrl2 = wx.TextCtrl(panel, -1, pos=(50, 10), size=(100, 20))
# # btn_ctrl = wx.Button(panel, -1, "Browse", pos=(160, 10))

# hbox = wx.BoxSizer(wx.HORIZONTAL)
# fgs = wx.FlexGridSizer(1, 2, 10, 10)

# st1 = wx.StaticText(panel, label="st1")
# st2 = wx.StaticText(panel, label="st2")

# fgs.AddMany(
#     [
#         (st1),
#         (st2),
#     ]
# )
# fgs.AddGrowableCol(1, 1)
# hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
# panel.SetSizer(hbox)

# frm.Show()

# app.MainLoop()

# import wx

# app = wx.App()
# frame = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.CLOSE_BOX)
# panel = wx.Panel(frame, -1)
# panel.SetBackgroundColour("green")
# hbox = wx.BoxSizer(wx.HORIZONTAL)
# hbox.SetBackgroundColour("yellow")
# frame.Show(True)
# app.MainLoop()


# import wx


# class MyWindow(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, "MyTitle")
#         panel1 = wx.Panel(self)
#         panel1.SetBackgroundColour("red")
#         panel2 = wx.Panel(self)
#         panel2.SetBackgroundColour("blue")
#         panel3 = wx.Panel(self)
#         panel3.SetBackgroundColour("green")
#         panel4 = wx.Panel(self)
#         panel4.SetBackgroundColour("yellow")
#         sz = wx.BoxSizer(wx.VERTICAL)
#         sz.Add(panel1, 1, wx.EXPAND)
#         sz.Add(panel2, 1, wx.EXPAND)
#         sz.Add(panel3, 1, wx.EXPAND)
#         sz.Add(panel4, 1, wx.EXPAND)
#         self.SetSizer(sz)


# if __name__ == "__main__":
#     app = wx.PySimpleApp()
#     frame = MyWindow(parent=None, id=-1)
#     frame.Show()
# app.MainLoop()


import wx

# アプリケーションの初期化
application = wx.App()

# Frameの生成
# 引数は(親ウィンドウ,識別子,タイトル)
frame = wx.Frame(None, wx.ID_ANY, "テストフレーム", size=(300, 300))

# パネル(赤)を生成
r_panel = wx.Panel(frame, wx.ID_ANY)
r_panel.SetBackgroundColour("#FF0000")

# パネル(緑)を生成
g_panel = wx.Panel(frame, wx.ID_ANY)
g_panel.SetBackgroundColour("#00FF00")

# パネル(青)を生成
b_panel = wx.Panel(frame, wx.ID_ANY)
b_panel.SetBackgroundColour("#0000FF")

# Sizerで横並びに配置
layout = wx.BoxSizer(wx.HORIZONTAL)

# Sizerにパネルを追加
# 引数は(追加対象,リサイズの有無(1or0),配置方法)
layout.Add(r_panel, 1, wx.EXPAND)
layout.Add(g_panel, 1, wx.EXPAND)
layout.Add(b_panel, 1, wx.EXPAND)

# FrameにSizerを紐づける
frame.SetSizer(layout)

# Frameの可視化
frame.Show()

# イベントの待ち受け状態への遷移
application.MainLoop()


import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(200, 300))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        vbox = wx.wx.BoxSizer(wx.VERTICAL)
        l1 = wx.StaticText(p, label="Enter a number", style=wx.ALIGN_CENTRE)
        vbox.Add(l1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)
        b1 = wx.Button(p, label="Btn1")
        vbox.Add(b1, 0, wx.EXPAND)

        b2 = wx.Button(p, label="Btn2")
        vbox.Add(b2, 0, wx.ALIGN_CENTER_HORIZONTAL)
        t = wx.TextCtrl(p)
        vbox.Add(t, 1, wx.EXPAND, 10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(p, label="Label2", style=wx.ALIGN_CENTRE)

        hbox.Add(l2, 0, wx.EXPAND)
        b3 = wx.Button(p, label="Btn3")
        hbox.AddStretchSpacer(1)
        hbox.Add(b3, 0, wx.ALIGN_LEFT, 20)
        vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)
        p.SetSizer(vbox)


app = wx.App()
Example(None, title="BoxSizer demo")
app.MainLoop()