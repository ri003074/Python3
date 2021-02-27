from pptx import Presentation
from pptx.util import Inches
from PIL import Image
import math


class PowerPoint:
    def __init__(self, pic_per_page):
        self.file_path = "./pictures/"
        self.file_names = [
            "b.png",
            "e.jpg",
            "e.jpg",
            "b.png",
            "e.jpg",
            "b.png",
            "e.jpg",
        ]
        self.slide_templace = "sample_slide.pptx"
        self.output_filename = "class_output.pptx"
        self.image_display_height = Inches(2.0)
        self.image_display_width = 0
        self.aspect_ratio = 0
        self.num_of_slides = 0
        self.pic_per_page = pic_per_page
        self.presentaition = Presentation(self.slide_templace)
        self.slide_width = self.presentaition.slide_width
        self.slide_height = self.presentaition.slide_height
        self.slide_layout = self.presentaition.slide_layouts[5]
        self.pic_top_offset = 0
        # self.pic_top_offset = -1000000

    def calc_aspect_ratio(self, file_name):
        # 画像サイズを取得してアスペクト比を得る
        im = Image.open(self.file_path + file_name)
        im_width, im_height = im.size
        self.aspect_ratio = im_width / im_height

    def calc_image_display_width(self):
        self.image_display_width = self.aspect_ratio * self.image_display_height

    def add_picture(self, slide, file_name, left, top):
        slide.shapes.add_picture(
            self.file_path + file_name,
            left,
            top,
            height=self.image_display_height,
        )

    def add_title(self, slide, file_name):
        title = slide.placeholders[0]
        title.text = file_name
        title.text = file_name.replace(".png", "").replace(".jpg", "")

    def make_pptx(self):

        if self.pic_per_page == 1:
            self.make_pptx_one_pic_per_slide()
        elif (
            self.pic_per_page == 2
            or self.pic_per_page == 3
            or self.pic_per_page == 4
            or self.pic_per_page == 6
        ):
            self.make_pptx_two_or_more_pic_per_slide()
        else:
            print("Error")

    def make_pptx_one_pic_per_slide(self):
        self.num_of_slides = len(self.file_names)
        for i in range(0, self.num_of_slides, self.pic_per_page):
            slide = self.presentaition.slides.add_slide(self.slide_layout)

            # 貼り付ける画像ファイル名を取得
            file_name = self.file_names[i]

            self.calc_aspect_ratio(file_name)
            self.calc_image_display_width()

            # センタリングする場合の画像の左上座標を計算
            left = (self.slide_width - self.image_display_width) / 2
            top = (self.slide_height - self.image_display_height) / 2

            self.add_picture(slide, file_name, left, top)

            # title
            self.add_title(slide, file_name)

        self.presentaition.save(self.output_filename)

    def make_pptx_two_or_more_pic_per_slide(self):
        self.num_of_slides = int(math.ceil(len(self.file_names) / self.pic_per_page))
        for i in range(0, self.num_of_slides * 2 + 3, self.pic_per_page):
            slide = self.presentaition.slides.add_slide(self.slide_layout)

            for j in range(0, self.pic_per_page):
                # 貼り付ける画像ファイル名を取得
                try:
                    file_name = self.file_names[i + j]
                except IndexError:
                    break

                self.calc_aspect_ratio(file_name)
                self.calc_image_display_width()

                if self.pic_per_page == 2 and j == 0:
                    # 1スライドに２枚貼り付ける場合の１枚目
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 2 and j == 1:
                    # 1スライドに２枚貼り付ける場合の2枚目
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 0:
                    # 1スライドに3枚貼り付ける場合の１枚目
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 1:
                    # 1スライドに3枚貼り付ける場合の2枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 2:
                    # 1スライドに3枚貼り付ける場合の3枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 0:
                    # 1スライドに4枚貼り付ける場合の１枚目
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 1:
                    # 1スライドに4枚貼り付ける場合の2枚目
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 2:
                    # 1スライドに4枚貼り付ける場合の3枚目
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 3:
                    # 1スライドに4枚貼り付ける場合の4枚目
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 0:
                    # 1スライドに6枚貼り付ける場合の１枚目
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 1:
                    # 1スライドに6枚貼り付ける場合の2枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 2:
                    # 1スライドに6枚貼り付ける場合の3枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 3:
                    # 1スライドに6枚貼り付ける場合の4枚目
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 4:
                    # 1スライドに6枚貼り付ける場合の5枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 5:
                    # 1スライドに6枚貼り付ける場合の6枚目
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                self.add_picture(slide, file_name, left, top)

                # テキストを追加
                width = height = Inches(1)
                print(top)
                print(top * 0.8)
                txBox = slide.shapes.add_textbox(left, top - 400000, width, height)
                tf = txBox.text_frame
                tf.text = file_name.replace(".png", "").replace(".jpg", "")

        self.presentaition.save(self.output_filename)


pptx = PowerPoint(pic_per_page=3)
pptx.make_pptx()
