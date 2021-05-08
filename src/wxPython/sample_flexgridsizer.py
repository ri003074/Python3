import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 170))

        self.folder1 = ""
        self.folder2 = ""
        self.folder3 = ""

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(4, 3, 10, 10)

        blank1 = wx.StaticText(panel, label="")
        blank2 = wx.StaticText(panel, label="")
        left = wx.StaticText(panel, label="left")
        center = wx.StaticText(panel, label="center")
        right = wx.StaticText(panel, label="right")

        self.tc1 = wx.TextCtrl(panel)
        self.tc2 = wx.TextCtrl(panel)
        self.tc3 = wx.TextCtrl(panel)

        btn1 = wx.Button(panel, label="browse")
        btn1.Bind(wx.EVT_BUTTON, self.file_browse1)

        btn2 = wx.Button(panel, label="browse")
        btn2.Bind(wx.EVT_BUTTON, self.file_browse2)

        btn3 = wx.Button(panel, label="browse")
        btn3.Bind(wx.EVT_BUTTON, self.file_browse3)

        btn4 = wx.Button(panel, label="execute")
        btn4.Bind(wx.EVT_BUTTON, self.close)

        fgs.AddMany(
            [
                (left),
                (self.tc1, 1, wx.EXPAND),
                (btn1),
                (center),
                (self.tc2, 1, wx.EXPAND),
                (btn2),
                (right, 1),
                (self.tc3, 1, wx.EXPAND),
                (btn3),
                (blank1),
                (blank2),
                (btn4),
            ]
        )
        # fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def file_browse1(self, event):
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.tc1.SetLabel(folder_path)
            self.folder1 = folder_path
        folder.Destroy()

    def file_browse2(self, event):
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.tc2.SetLabel(folder_path)
            self.folder2 = folder_path
        folder.Destroy()

    def file_browse3(self, event):
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.tc3.SetLabel(folder_path)
            self.folder3 = folder_path
        folder.Destroy()

    def close(self, event):
        self.Close()


app = wx.App()
obj = Example(None, title="select dir")
app.MainLoop()
