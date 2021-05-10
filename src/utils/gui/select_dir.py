import wx


class SelectDir(wx.Frame):
    def __init__(self, parent, title, folder_count):
        super(SelectDir, self).__init__(parent, title=title)
        MAX_FOLDER_COUNT = 4
        self.folder = [""] * MAX_FOLDER_COUNT
        self.folder_count = folder_count
        self.text_ctrl = []
        self.arr = []
        self.btn = []
        self.static_text = []
        self.radio_box = []
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

        for text_ctrl in self.text_ctrl:
            text_ctrl.Destroy()

        for btn in self.btn:
            btn.Destroy()

        for static_text in self.static_text:
            static_text.Destroy()

        self.btn = []
        self.static_text = []
        self.arr = []
        self.text_ctrl = []
        for i in range(self.folder_count):
            self.text_ctrl.append(wx.TextCtrl(self, size=(400, -1)))
            self.static_text.append(
                wx.StaticText(self, label=eval(f"self.label{self.folder_count}[i]"))
            )
            self.btn.append(wx.Button(self, label="browse"))
            self.btn[i].Bind(wx.EVT_BUTTON, self.folder_browse)
            self.btn[i].index = i
            self.arr.append(self.static_text[i])
            self.arr.append([self.text_ctrl[i], 1, wx.EXPAND])
            self.arr.append(self.btn[i])

        if self.btn_exe:
            self.btn_exe.Destroy()

        self.btn_exe = wx.Button(self, label="execute")
        self.btn_exe.Bind(wx.EVT_BUTTON, self.close)

        if self.radio_box:
            self.radio_box.Destroy()

        self.radio_box = wx.RadioBox(self, -1, choices=["1", "2", "3", "4"])
        self.radio_box.Bind(wx.EVT_RADIOBOX, self.check)
        self.radio_box.EnableItem(self.folder_count - 1, False)
        self.radio_box.SetSelection(self.folder_count - 1)

        self.arr.append(self.radio_box)
        self.arr.append(blank1)
        self.arr.append(self.btn_exe)
        fgs.AddMany(self.arr)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(hbox)
        self.Fit()

    def folder_browse(self, event):
        btn = event.GetEventObject()
        index = btn.index
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.text_ctrl[index].SetLabel(folder_path)
            self.folder[index] = folder_path

        # folder.Destroy()

    def close(self, event):
        self.Close()

    def check(self, event):
        num = self.radio_box.GetSelection()
        self.folder_count = num + 1
        self.InitUI()


if __name__ == "__main__":
    app = wx.App()
    select_dir = SelectDir(None, title="select dir", folder_count=1)
    app.MainLoop()
    print(select_dir.folder[0])
    print(select_dir.folder[1])
    # print(select_dir.folder[2])
