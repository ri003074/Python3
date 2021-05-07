import win32com.client

pptx = win32com.client.Dispatch("PowerPoint.Application")  # active presentation

active_presentation = pptx.ActivePresentation

print(active_presentation.Slides(1).Layout)

active_presentation.Slides.Add(2, 32)
