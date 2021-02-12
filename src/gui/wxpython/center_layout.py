import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)
        layout = wx.BoxSizer(wx.VERTICAL)
        close_button = wx.Button(panel, label="Close")
        close_button.Bind(wx.EVT_BUTTON, self.on_close)
        layout.AddStretchSpacer()
        text = wx.StaticText(panel, -1, "This is example")
        layout.Add(text, flag=wx.CENTER)
        layout.Add(close_button, flag=wx.CENTER)
        layout.AddStretchSpacer()
        panel.SetSizer(layout)

    def on_close(self, e):
        self.Close(True)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
