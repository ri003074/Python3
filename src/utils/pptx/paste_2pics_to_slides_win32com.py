import win32com.client
import os
import glob

pptx = win32com.client.Dispatch("PowerPoint.Application")  # active presentation
# pptx = win32com.client.GetObject(Class="PowerPoint.Application") # activate pptx

active_presentation = pptx.ActivePresentation
pptx_file_name = active_presentation.Name
print(pptx_file_name)

pptx_width = active_presentation.PageSetup.SlideWidth
pptx_height = active_presentation.PageSetup.SlideHeight
image_width = (pptx_width / 2) * 0.8
image_left_position_offset = pptx_width / 2 * 0.1
image_top_position = pptx_height * 0.4
textbox_top_position = image_top_position - 50
textbox_width = 200
textbox_height = 100

slide_count = active_presentation.Slides.Count
images = glob.glob("imgs/*")

image_counter = 0
for i in range(slide_count + 1, slide_count + 1 + int(len(images) / 2)):
    active_presentation.Slides.Add(i, 11)

    # title
    active_presentation.Slides(i).Shapes.Placeholders.Item(
        1
    ).TextFrame.TextRange.Text = "abc"

    # first image and file name
    inserted_txtbox = active_presentation.Slides(i).Shapes.AddTextbox(
        1,
        pptx_width / 4 - textbox_width / 2,
        textbox_top_position,
        textbox_width,
        textbox_width,
    )
    image_name = images[image_counter]
    image_name = image_name.replace("imgs\\", "").replace(".PNG", "")
    inserted_txtbox.TextFrame.TextRange.Text = image_name
    inserted_txtbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # 中央ぞろえ

    inserted_imgs = active_presentation.Slides(i).Shapes.AddPicture(
        FileName=os.getcwd() + "/" + images[image_counter],
        LinkToFile=-1,
        SaveWithDocument=-1,
        Left=image_left_position_offset,
        Top=image_top_position,
    )
    inserted_imgs.Width = image_width
    image_counter += 1

    # second image and file name
    inserted_txtbox = active_presentation.Slides(i).Shapes.AddTextbox(
        1,
        pptx_width * 3 / 4 + -textbox_width / 2,
        textbox_top_position,
        textbox_width,
        textbox_height,
    )
    image_name = images[image_counter]
    image_name = image_name.replace("imgs\\", "").replace(".PNG", "")
    inserted_txtbox.TextFrame.TextRange.Text = image_name
    inserted_txtbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # 中央ぞろえ
    inserted_imgs = active_presentation.Slides(i).Shapes.AddPicture(
        FileName=os.getcwd() + "/" + images[image_counter],
        LinkToFile=-1,
        SaveWithDocument=-1,
        Left=pptx_width / 2 + image_left_position_offset,
        Top=image_top_position,
    )
    inserted_imgs.Width = image_width
    image_counter += 1
