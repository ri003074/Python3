import win32com.client

pptx = win32com.client.GetActiveObject("PowerPoint.Application")
active_presentation = pptx.ActivePresentation

for i in range(1, 3):
    active_presentation.Slides.Add(Index=i, Layout=12)
    active_presentation.SectionProperties.AddBeforeSlide(
        SlideIndex=i, sectionName="abc"
    )
