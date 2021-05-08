import wx

app = wx.App()

frm = wx.Frame(None, title="hello")

panel = wx.Panel(frm, -1)
text_ctrl1 = wx.StaticText(panel, -1, pos=(10, 10), size=(40, 10), label="Left")
text_ctrl2 = wx.TextCtrl(panel, -1, pos=(50, 10), size=(100, 20))
btn_ctrl = wx.Button(panel, -1, "Browse", pos=(160, 10))

frm.Show()

app.MainLoop()
