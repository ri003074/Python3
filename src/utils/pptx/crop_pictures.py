import win32com.client

pptx = win32com.client.GetActiveObject("PowerPoint.Application")
active_presentation = pptx.ActivePresentation

for i in range(1, active_presentation.Slides.Count + 1):
    for j in range(1, active_presentation.Slides(i).Shapes.Count + 1):
        if active_presentation.Slides(i).Shapes(j).Width < 300:  # Cropする画像の条件
            pf = active_presentation.Slides(i).Shapes(j).PictureFormat
            pf.CropTop = 20
            pf.CropLeft = 20
            pf.CropBottom = 20
            pf.CropRight = 20
