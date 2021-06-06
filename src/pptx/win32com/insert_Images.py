import win32com.client
import os
import glob


images = glob.glob("../imgs/*")


class InsertImages:
    def __init__(self):
        # pptx = win32com.client.GetObject(Class="PowerPoint.Application") # activate pptx
        pptx = win32com.client.Dispatch("PowerPoint.Application")  # active presentation
        self.active_presentation = pptx.ActivePresentation
        self.slide_width = self.active_presentation.PageSetup.SlideWidth
        self.slide_height = self.active_presentation.PageSetup.SlideHeight

    def insert_image(self, *argv):
        image_width = self.slide_width * 0.6

        image_per_slide = len(argv)
        if image_per_slide == 1:
            for i in range(0, len(argv[0])):
                slide_num = i + 1
                self.active_presentation.Slides.Add(slide_num, 11)
                # title
                image_name = argv[0][i]
                title = image_name.replace("imgs\\", "").replace(".PNG", "")
                self.active_presentation.Slides(slide_num).Shapes.Placeholders.Item(
                    1
                ).TextFrame.TextRange.Text = title

                self.add_image(
                    file_name=image_name,
                    slide_num=slide_num,
                    left=self.slide_width / 2 - image_width / 2,
                    top=self.slide_height * 0.2,
                    width=image_width,
                )
                # first image and file name
                inserted_imgs = self.active_presentation.Slides(
                    slide_num
                ).Shapes.AddPicture(
                    FileName=os.getcwd() + "/" + argv[0][i],
                    LinkToFile=-1,
                    SaveWithDocument=-1,
                    Left=self.slide_width / 2 - image_width / 2,
                    Top=self.slide_height * 0.2,
                )
                inserted_imgs.Width = image_width

        elif image_per_slide == 2:
            image_width = 380
            image_top_position = self.slide_height * 0.3
            image_left_position_img1 = self.slide_width / 4 - image_width / 2
            image_left_position_img2 = self.slide_width * 3 / 4 - image_width / 2
            text_box_height = 10

            for i in range(0, len(argv[0])):
                slide_num = i + 1
                image_name1 = argv[0][i]
                image_name2 = argv[1][i]
                self.active_presentation.Slides.Add(slide_num, 11)

                self.add_image(
                    file_name=image_name1,
                    slide_num=slide_num,
                    left=image_left_position_img1,
                    top=image_top_position,
                    width=image_width,
                )

                self.add_textbox(
                    title=image_name1,
                    slide_num=slide_num,
                    top=image_top_position,
                    left=image_left_position_img1,
                    width=image_width,
                    height=text_box_height,
                )

                self.add_image(
                    file_name=image_name2,
                    slide_num=slide_num,
                    left=image_left_position_img2,
                    top=image_top_position,
                    width=image_width,
                )
                self.add_textbox(
                    title=image_name2,
                    slide_num=slide_num,
                    top=image_top_position,
                    left=image_left_position_img2,
                    width=image_width,
                    height=text_box_height,
                )

    def add_textbox(self, title, slide_num, top, left, width, height):
        inserted_txtbox = self.active_presentation.Slides(slide_num).Shapes.AddTextbox(
            1, Top=top, Left=left, Width=width, Height=height,
        )
        inserted_txtbox.TextFrame.TextRange.Text = title
        inserted_txtbox.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # 中央ぞろえ

        inserted_txtbox.Top = inserted_txtbox.Top - inserted_txtbox.Height

    def add_image(self, file_name, slide_num, left, top, width):
        # title
        image_name = file_name
        image_name = image_name.replace("imgs\\", "").replace(".PNG", "")
        self.active_presentation.Slides(slide_num).Shapes.Placeholders.Item(
            1
        ).TextFrame.TextRange.Text = image_name

        # first image and file name
        inserted_imgs = self.active_presentation.Slides(slide_num).Shapes.AddPicture(
            FileName=os.getcwd() + "/" + file_name,
            LinkToFile=-1,
            SaveWithDocument=-1,
            Left=left,
            Top=top,
        )

        # keep aspect ratio
        inserted_imgs.Width = width


aa = InsertImages()
aa.insert_image(images, images)
