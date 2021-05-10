import wx


class SelectFile(wx.Frame):
    def __init__(self, parent, title, file_count):
        super(SelectFile, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(1, 3, 10, 10)

        st = wx.StaticText(self, label="file1")
        tc = wx.TextCtrl(self, size=(400, -1))
        btn = wx.Button(self, label="browse")
        btn.Bind(wx.EVT_BUTTON, self.file_browse)

        fgs.AddMany([st, tc, btn])
        hbox.Add(fgs, proportion=2, flag=wx.ALL, border=10)
        self.SetSizer(hbox)
        self.Fit()

    def file_browse(self, event):
        # if self.contentNotSaved:
        #     if (
        #         wx.MessageBox(
        #             "Current content has not been saved! Proceed?",
        #             "Please confirm",
        #             wx.ICON_QUESTION | wx.YES_NO,
        #             self,
        #         )
        #         == wx.NO
        #     ):
        #         return

        # otherwise ask the user what new file to open
        with wx.FileDialog(
            self,
            "select file",
            wildcard="*.pdf",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # get full path of the file
            pathname = fileDialog.GetPath()
            print(pathname)


if __name__ == "__main__":
    app = wx.App()
    select_file = SelectFile(None, title="select file", file_count=1)
    app.MainLoop()