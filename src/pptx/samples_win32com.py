# import win32com.client

# pptx = win32com.client.Dispatch("PowerPoint.Application")
# pptx.Visible = True
# active_presentation = pptx.Presentations.Add()

# pptx = win32com.client.GetActiveObject("PowerPoint.Application")
# active_presentation = pptx.ActivePresentation
# print(active_presentation.Slides.Count)

# for i in range(1, active_presentation.Slides.Count + 1):
#     print(active_presentation.Slides(i).Layout)

# for i in range(len(active_presentation.Slides)):
#     print(i)


# active_presentation.Slides.Add(4, 11)

# print(active_presentation.Slides(1).Shapes.Count)

# print(active_presentation.Slides(1).Shapes(1).TextFrame.TextRange.Text)
# active_presentation.Slides(1).Shapes(1).TextFrame.TextRange.Text = "abc"

# import win32com.client

# pptx = win32com.client.Dispatch("PowerPoint.Application")
# pptx.Visible = True
# active_presentation = pptx.Presentations.Add()
# active_presentation.Slides.Add(1, 11)
# active_presentation.Slides(1).Shapes(1).TextFrame.TextRange.Text = "first presentation"


# import win32com.client

# pptx = win32com.client.Dispatch("PowerPoint.Application")
# pptx.Visible = True
# active_presentation = pptx.Presentations.Add()
# active_presentation.Slides.Add(1, 14)
# for i in range(active_presentation.Slides(1).Shapes.Count):
#     print(active_presentation.Slides(1).Shapes(1).Type)


# import win32com.client

# pptx = win32com.client.Dispatch("PowerPoint.Application")
# pptx.Visible = True
# active_presentation = pptx.Presentations.Add()
# print(active_presentation.PageSetup.SlideWidth)
# active_presentation.Slides.Add(1, 12)
# textbox = active_presentation.Slides(1).Shapes.AddTextbox(
#     1, 0, 0, active_presentation.PageSetup.SlideWidth, 100
# )
# textbox.TextFrame.TextRange.Text = "text box"
# textbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2

# import win32com.client
# import os

# pptx = win32com.client.Dispatch("PowerPoint.Application")
# pptx.Visible = True
# active_presentation = pptx.Presentations.Add()
# active_presentation.Slides.Add(1, 12)
# image = active_presentation.Slides(1).Shapes.AddPicture(
#     FileName=os.getcwd() + "/imgs/sample1.PNG",
#     LinkToFile=-1,
#     SaveWithDocument=-1,
#     Left=0,
#     Top=0,
# )
# image.Width = 500

import win32com.client

pptx = win32com.client.Dispatch("PowerPoint.Application")
pptx.Visible = True
active_presentation = pptx.Presentations.Add()
slide_width = active_presentation.PageSetup.SlideWidth
slide_width = active_presentation.PageSetup.SlideHeight
