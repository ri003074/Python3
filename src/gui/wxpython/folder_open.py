import wx


class Main(wx.Frame):
    def __init__(self, parent, id, title):
        self.old_path = ""

        wx.Frame.__init__(self, parent, id, title, size=(500, 300))
        panel = wx.Panel(self, id=wx.ID_ANY)

        # 旧プロジェクトファイル選択ボタン
        wx.StaticText(panel, wx.ID_ANY, label="旧プロジェクト", pos=(10, 10))
        self.old = wx.TextCtrl(panel, wx.ID_ANY, pos=(10, 30), size=(320, 20))
        choose_button_old = wx.Button(panel, label="フォルダの選択", pos=(350, 30))
        choose_button_old.Bind(wx.EVT_BUTTON, self.choose_folder_old)

        # 最新プロジェクトファイル選択ボタン
        wx.StaticText(panel, wx.ID_ANY, label="最新プロジェクト", pos=(10, 60))
        self.latest = wx.TextCtrl(panel, wx.ID_ANY, pos=(10, 80), size=(320, 20))
        choose_button_latest = wx.Button(panel, label="フォルダの選択", pos=(350, 80))
        choose_button_latest.Bind(wx.EVT_BUTTON, self.choose_folder_latest)

        close_button = wx.Button(panel, label="execute", pos=(350, 100))
        close_button.Bind(wx.EVT_BUTTON, self.close)

        # 画面を表示
        self.Show(True)
        # 画面の表示位置を中央に
        self.Centre()

    def choose_folder_old(self, event):
        """ フォルダの選択ボタンを押すと呼ばれるイベント。フォルダ選択ダイアログを開き、choose_textに反映 """

        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR, message="保存先フォルダ")

        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
        folder.Destroy()
        self.old.SetLabel(folder_path)
        self.old_path = folder_path

    def choose_folder_latest(self, event):
        """ フォルダの選択ボタンを押すと呼ばれるイベント。フォルダ選択ダイアログを開き、choose_textに反映 """

        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR, message="保存先フォルダ")

        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
        folder.Destroy()
        self.latest.SetLabel(folder_path)

    def close(self, event):
        self.Close(True)


def main():
    app = wx.App(False)
    aa = Main(None, wx.ID_ANY, "Project Updater")
    app.MainLoop()
    print(aa.old_path)


if __name__ == "__main__":
    main()
