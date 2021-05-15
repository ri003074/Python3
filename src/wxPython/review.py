#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create review
layout with wx.FlexGridSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.SetMinSize(10, 10)

        # fgs = wx.FlexGridSizer(2, 2, 9, 25)
        fgs = wx.FlexGridSizer(2, 2, 10, 10)
        fgs.SetMinSize(1, 1)

        title = wx.StaticText(panel, label="Title")
        author = wx.StaticText(panel, label="Author")

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)

        fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author), (tc2, 1, wx.EXPAND)])

        fgs.AddGrowableRow(1)
        fgs.AddGrowableCol(1)
        # fgs.SetSizeHints(self)

        hbox.Add(fgs, proportion=1, flag=wx.ALL, border=15)
        # hbox.FitInside(panel)
        # panel.SetSizeHints(self)
        panel.SetSizer(hbox)
        hbox.SetSizeHints(self)
        # panel.FitInside()


def main():

    app = wx.App()
    ex = Example(None, title="Review")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
