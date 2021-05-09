import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        # self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        # vbox.Add(self.display, flag=wx.EXPAND)
        gs = wx.GridSizer(2, 3, 10, 10)
        gs.AddMany(
            [
                (wx.Button(self, label="bck0")),
                (wx.Button(self, label="bck1")),
                (wx.Button(self, label="bck2")),
                (wx.Button(self, label="bck3")),
                (wx.Button(self, label="bck4")),
                (wx.Button(self, label="bck5")),
            ]
        )
        vbox.Add(gs, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)
        self.SetSizer(vbox)
        self.Fit()


def main():
    app = wx.App()
    ex = Example(None, title="Calculator")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()