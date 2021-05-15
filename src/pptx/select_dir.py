import wx


class SelectDir(wx.Frame):
    def __init__(self, parent, title, folder_count):
        super(SelectDir, self).__init__(parent, title=title, size=(500, 170))

        self.folder = [""] * folder_count
        self.tc = [""] * folder_count
        self.folder_count = folder_count

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(4, 3, 10, 10)

        blank1 = wx.StaticText(panel, label="")
        blank2 = wx.StaticText(panel, label="")

        btn = []
        st = []
        arr = []
        for i in range(self.folder_count):
            self.tc[i] = wx.TextCtrl(panel)
            st.append(wx.StaticText(panel, label="folder" + str(i)))
            btn.append(wx.Button(panel, label="browse"))
            btn[i].Bind(wx.EVT_BUTTON, self.file_browse)
            btn[i].index = i
            arr.append(st[i])
            arr.append((self.tc[i], 1, wx.EXPAND))
            arr.append(btn[i])

        btn4 = wx.Button(panel, label="execute")
        btn4.Bind(wx.EVT_BUTTON, self.close)

        arr.append(blank1)
        arr.append(blank2)
        arr.append(btn4)
        fgs.AddMany(arr)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def file_browse(self, event):
        btn = event.GetEventObject()
        index = btn.index
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR)
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
            self.tc[index].SetLabel(folder_path)
            self.folder[index] = folder_path
        folder.Destroy()

    def close(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    select_dir = SelectDir(None, title="select dir", folder_count=3)
    app.MainLoop()
    print(select_dir.folder[0])
    print(select_dir.folder[1])
    # print(select_dir.folder[2])
