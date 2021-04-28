import win32com.client
import os
import glob

pptx = win32com.client.Dispatch("PowerPoint.Application")  # active presentation
# pptx = win32com.client.GetObject(Class="PowerPoint.Application") # activate pptx

active_presentation = pptx.ActivePresentation

PPTX_WIDTH = active_presentation.PageSetup.SlideWidth
PPTX_HEIGHT = active_presentation.PageSetup.SlideHeight
IMAGE_WIDTH = (PPTX_WIDTH / 2) * 0.8
IMGAGE_LEFT_POSITION = PPTX_WIDTH / 2 * 0.1
IMAGE_TOP_POSITION = PPTX_HEIGHT * 0.4
TEXTBOX_TOP_POSITION = IMAGE_TOP_POSITION - 50
TEXTBOX_WIDTH = 200
TEXTBOX_HEIGHT = 100
CURRENT_SLIDE_COUNT = active_presentation.Slides.Count
images = glob.glob("imgs/*")
images2 = glob.glob("imgs2/*")
slide_titles = ["abc", "def"]


def insert_images_to_pptx(slide_titles, *argv):

    images_per_slide = len(argv)

    image_slide_start_number = CURRENT_SLIDE_COUNT + 1
    image_counter = 0
    if images_per_slide == 1:
        for i in range(
            image_slide_start_number, image_slide_start_number + len(argv[0]),
        ):
            active_presentation.Slides.Add(i, 11)
            # title
            image_name = argv[0][image_counter]
            image_name = image_name.replace("imgs\\", "").replace(".PNG", "")
            active_presentation.Slides(i).Shapes.Placeholders.Item(
                1
            ).TextFrame.TextRange.Text = slide_titles[i - CURRENT_SLIDE_COUNT - 1]

            # first image and file name
            inserted_imgs = active_presentation.Slides(i).Shapes.AddPicture(
                FileName=os.getcwd() + "/" + images[image_counter],
                LinkToFile=-1,
                SaveWithDocument=-1,
                Left=IMGAGE_LEFT_POSITION,
                Top=IMAGE_TOP_POSITION,
            )
            inserted_imgs.Width = IMAGE_WIDTH
            image_counter += 1

    elif images_per_slide == 2:
        for i in range(
            image_slide_start_number, image_slide_start_number + len(argv[0]),
        ):
            active_presentation.Slides.Add(i, 11)
            # title
            image_name = argv[0][image_counter]
            # first image and file name
            inserted_imgs = active_presentation.Slides(i).Shapes.AddPicture(
                FileName=os.getcwd() + "/" + image_name,
                LinkToFile=-1,
                SaveWithDocument=-1,
                Left=IMGAGE_LEFT_POSITION,
                Top=IMAGE_TOP_POSITION,
            )
            inserted_imgs.Width = IMAGE_WIDTH

            image_name = image_name.replace("imgs\\", "").replace(".PNG", "")
            active_presentation.Slides(i).Shapes.Placeholders.Item(
                1
            ).TextFrame.TextRange.Text = slide_titles[i - CURRENT_SLIDE_COUNT - 1]
            inserted_txtbox = active_presentation.Slides(i).Shapes.AddTextbox(
                1,
                PPTX_WIDTH * 1 / 4 + -TEXTBOX_WIDTH / 2,
                TEXTBOX_TOP_POSITION,
                TEXTBOX_WIDTH,
                TEXTBOX_HEIGHT,
            )
            inserted_txtbox.TextFrame.TextRange.Text = image_name
            inserted_txtbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # 中央ぞろえ

            # title
            image_name = argv[1][image_counter]
            # second image and file name
            inserted_imgs = active_presentation.Slides(i).Shapes.AddPicture(
                FileName=os.getcwd() + "/" + image_name,
                LinkToFile=-1,
                SaveWithDocument=-1,
                Left=IMGAGE_LEFT_POSITION + PPTX_WIDTH / 2,
                Top=IMAGE_TOP_POSITION,
            )
            inserted_imgs.Width = IMAGE_WIDTH
            image_name = image_name.replace("imgs2\\", "").replace(".PNG", "")
            inserted_txtbox = active_presentation.Slides(i).Shapes.AddTextbox(
                1,
                PPTX_WIDTH * 3 / 4 + -TEXTBOX_WIDTH / 2,
                TEXTBOX_TOP_POSITION,
                TEXTBOX_WIDTH,
                TEXTBOX_HEIGHT,
            )
            inserted_txtbox.TextFrame.TextRange.Text = image_name
            inserted_txtbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # 中央ぞろえ

            image_counter += 1


insert_images_to_pptx(slide_titles, images, images2)
# insert_images_to_pptx(slide_titles, images)
