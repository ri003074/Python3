import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.subs = []
        self.rbox = []
        self.checked_box = 0
        self.InitUI()
        self.InitUI()
        self.Centre()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        for a in self.subs:
            print(type(a))
            a.Destroy()

        self.subs = []
        if self.rbox:
            self.rbox.Destroy()
        self.rbox = wx.RadioBox(self, -1, choices=["choice 1", "choice 2"])
        self.rbox.Bind(wx.EVT_RADIOBOX, self.check)
        self.rbox.EnableItem(self.checked_box, False)
        self.rbox.SetSelection(0)
        # self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        # vbox.Add(self.display, flag=wx.EXPAND)
        self.subs.append(self.rbox)
        self.subs.append(wx.Button(self, label="bck0"))
        self.subs.append(wx.Button(self, label="bck1"))
        self.subs.append(wx.Button(self, label="bck2"))
        self.subs.append(wx.Button(self, label="bck3"))
        self.subs.append(wx.Button(self, label="bck4"))
        self.subs.append(wx.Button(self, label="bck5"))
        gs = wx.GridSizer(2, 4, 10, 10)
        gs.AddMany(self.subs)
        vbox.Add(gs, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)
        self.SetSizer(vbox)
        self.Fit()

    def InitUI2(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        # self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        # vbox.Add(self.display, flag=wx.EXPAND)
        for a in vbox:
            print(a)
        gs = wx.GridSizer(1, 4, 10, 10)

        for a in self.subs:
            print(type(a))
            a.Destroy()

        self.subs = []
        if self.rbox:
            self.rbox.Destroy()
        self.rbox = wx.RadioBox(self, -1, choices=["choice 1", "choice 2"])
        self.rbox.Bind(wx.EVT_RADIOBOX, self.check)
        self.rbox.EnableItem(self.checked_box, False)
        self.rbox.SetSelection(1)

        self.subs.append(self.rbox)
        self.subs.append(wx.Button(self, label="bck0"))
        self.subs.append(wx.Button(self, label="bck1"))
        self.subs.append(wx.Button(self, label="bck2"))

        gs.AddMany(self.subs)
        vbox.Add(gs, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)
        self.SetSizer(vbox)
        self.Fit()

    def check(self, evt):
        num = self.rbox.GetSelection()
        self.checked_box = num
        # for i in range(self.chce.GetCount()):
        #     self.chce.Delete(0)
        if num == 0:
            # for i in range(3):
            #     self.chce.Append(self.cc1[i])  # ここでリストを変える。
            self.InitUI()
        else:
            # for i in range(2):
            #     self.chce.Append(self.cc2[i])  # ここでリストを変える。
            self.InitUI2()
        # self.chce.SetSelection(0)  # リストの最初の項目を表示する


def main():
    app = wx.App()
    ex = Example(None, title="Calculator")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
