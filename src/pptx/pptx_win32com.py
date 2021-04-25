import win32com.client

pptx = win32com.client.Dispatch("PowerPoint.Application")  # active presentation
# pptx = win32com.client.GetObject(Class="PowerPoint.Application") # activate pptx

active_presentation = pptx.ActivePresentation
pptx_file_name = active_presentation.Name

print(pptx_file_name)

pptx_width = active_presentation.PageSetup.SlideWidth
pptx_height = active_presentation.PageSetup.SlideHeight
print(pptx_width)
print(pptx_height)

active_presentation.Slides.Add(2, 2)
