import wx

label1 = "Test label"


class MyApp(wx.PySimpleApp):
    def OnInit(self):
        Frm = wx.Frame(None, -1, "Title", size=(300, 250))
        self.p = p = wx.Panel(Frm, -1)

        self.rbox = wx.RadioBox(p, -1, "Test", choices=["choice 1", "choice 2"])
        self.rbox.Bind(wx.EVT_RADIOBOX, self.check)

        self.cc1 = ["1-1", "1-2", "1-3"]
        self.cc2 = ["2-1", "2-2", "2-3"]
        self.chce = wx.Choice(p, -1, choices=self.cc1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.rbox, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.chce, 0, wx.ALL | wx.CENTER, 10)

        p.SetSizer(sizer)
        Frm.Show()
        return 1

    def check(self, evt):
        num = self.rbox.GetSelection()
        for i in range(self.chce.GetCount()):
            self.chce.Delete(0)
        if num == 0:
            for i in range(3):
                self.chce.Append(self.cc1[i])  # ここでリストを変える。
        else:
            for i in range(2):
                self.chce.Append(self.cc2[i])  # ここでリストを変える。
        self.chce.SetSelection(0)  # リストの最初の項目を表示する


app = MyApp()
app.MainLoop()