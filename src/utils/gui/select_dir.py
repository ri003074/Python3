import wx


class SelectDir(wx.Frame):
    def __init__(self, parent, title, folder_count):
        super(SelectDir, self).__init__(parent, title=title)
        MAX_FOLDER_COUNT = 4
        self.folder = [""] * MAX_FOLDER_COUNT
        self.folder_count = folder_count
        self.tc = []
        self.arr = []
        self.btn = []
        self.st = []
        self.rbox = []
        self.btn_exe = []
        self.label1 = ["center"]
        self.label2 = ["left", "right"]
        self.label3 = ["left", "center", "right"]
        self.label4 = ["left top", "right top", "left bottom", "right bottom"]

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(self.folder_count + 1, 3, 10, 10)

        blank1 = wx.StaticText(self, label="")
        # blank2 = wx.StaticText(self, label="")

        for tc in self.tc:
            tc.Destroy()

        for btn in self.btn:
            btn.Destroy()

        for st in self.st:
            st.Destroy()

        self.btn = []
        self.st = []
        self.arr = []
        self.tc = []
        for i in range(self.folder_count):
            self.tc.append(wx.TextCtrl(self, size=(400, -1)))
            self.st.append(
                wx.StaticText(self, label=eval(f"self.label{self.folder_count}[i]"))
            )
            self.btn.append(wx.Button(self, label="browse"))
            self.btn[i].Bind(wx.EVT_BUTTON, self.folder_browse)
            self.btn[i].index = i
            self.arr.append(self.st[i])
            self.arr.append([self.tc[i], 1, wx.EXPAND])
            self.arr.append(self.btn[i])

        if self.btn_exe:
            self.btn_exe.Destroy()

        self.btn_exe = wx.Button(self, label="execute")
        self.btn_exe.Bind(wx.EVT_BUTTON, self.close)

        if self.rbox:
            self.rbox.Destroy()

        self.rbox = wx.RadioBox(self, -1, choices=["1", "2", "3", "4"])
        self.rbox.Bind(wx.EVT_RADIOBOX, self.check)
        self.rbox.EnableItem(self.folder_count - 1, False)
        self.rbox.SetSelection(self.folder_count - 1)

        self.arr.append(self.rbox)
        self.arr.append(blank1)
        self.arr.append(self.btn_exe)
        fgs.AddMany(self.arr)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(hbox)
        self.Fit()

    def folder_browse(self, event):
        self.btn = event.GetEventObject()
        index = self.btn.index
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.tc[index].SetLabel(folder_path)
            self.folder[index] = folder_path
        folder.Destroy()

    def close(self, event):
        self.Close()

    def check(self, event):
        num = self.rbox.GetSelection()
        self.folder_count = num + 1
        self.InitUI()


if __name__ == "__main__":
    app = wx.App()
    select_dir = SelectDir(None, title="select dir", folder_count=1)
    app.MainLoop()
    print(select_dir.folder[0])
    print(select_dir.folder[1])
    # print(select_dir.folder[2])
