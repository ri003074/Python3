import wx


class SampleFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(SampleFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        static_text_1 = wx.StaticText(panel, wx.ID_ANY, "ABC", style=wx.TE_CENTER)
        static_text_2 = wx.StaticText(panel, wx.ID_ANY, "DEF", style=wx.TE_CENTER)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(static_text_1, flag=wx.GROW)
        layout.Add(static_text_2, flag=wx.GROW)
        panel.SetSizer(layout)

        for key, value in kw.items():
            print("{0} = {1}".format(key, value))


if __name__ == "__main__":
    app = wx.App()
    frame = SampleFrame(None, title="sample", size=(200, 200))
    frame.Show()
    app.MainLoop()
