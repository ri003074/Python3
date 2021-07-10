import win32com.client
from icecream import ic


pptx = win32com.client.Dispatch("PowerPoint.Application")
active_presentation = pptx.ActivePresentation
slide_count = active_presentation.Slides.Count
ic(slide_count)

for i in range(1, slide_count + 1):
    shapes_per_slide = active_presentation.Slides(i).Shapes.Count
    for j in reversed(range(1, shapes_per_slide + 1)):
        shape_type = active_presentation.Slides(i).Shapes(j).Type
        ic(shape_type)
        if shape_type == 11:
            active_presentation.Slides(i).Shapes(j).Delete()
