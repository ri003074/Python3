import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "フローレイアウト", size=(400, 300))
panel = wx.Panel(frame, -1)
layout = wx.FlexGridSizer(rows=2, cols=2, gap=(0, 10))
panel.SetSizer(layout)

cmb_array = ("toyota", "honda", "mazda")
cmb = wx.ComboBox(panel, wx.ID_ANY, choices=cmb_array, style=wx.CB_DROPDOWN)
txt = wx.TextCtrl(panel, wx.ID_ANY)
txt1 = wx.StaticText(panel, wx.ID_ANY, label="left top")
layout.Add(txt1, wx.ALIGN_RIGHT)
layout.Add(txt, wx.ALIGN_RIGHT)
layout.Add(cmb)

frame.Show(True)

app.MainLoop()
