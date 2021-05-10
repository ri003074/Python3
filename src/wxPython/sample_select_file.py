import wx

class SelectFile(wx.Frame):
    def __init__(self, parent, title, file_count):
        super(SelectFile, self).__init__(parent, title=title)
        