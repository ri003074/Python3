from pptx import Presentation
from pptx.util import Inches
from PIL import Image
import math

file_list = [
    "b.png",
    "e.jpg",
    "e.jpg",
    "b.png",
    "e.jpg",
    "b.png",
    "e.jpg",
]

file_path = "./pictures/"


class PowerPoint:
    def __init__(self, files, file_path, pic_per_page, image_height, pic_top_offset=0):
        self.file_path = file_path
        self.files = files
        self.slide_template = "sample_slide.pptx"
        self.output_filename = "class_output.pptx"
        self.image_display_height = image_height
        self.image_display_width = 0
        self.aspect_ratio = 0
        self.num_of_slides = 0
        self.pic_per_page = pic_per_page
        self.presentaition = Presentation(self.slide_template)
        self.slide_width = self.presentaition.slide_width
        self.slide_height = self.presentaition.slide_height
        self.slide_layout = self.presentaition.slide_layouts[5]
        self.pic_top_offset = pic_top_offset
        # self.pic_top_offset = -1000000

    def calc_aspect_ratio(self, file_name):
        """ get image size and calculate aspect ratio"""
        im = Image.open(self.file_path + file_name)
        im_width, im_height = im.size
        self.aspect_ratio = im_width / im_height

    def calc_image_display_width(self):
        """ calculate image width """
        self.image_display_width = self.aspect_ratio * self.image_display_height

    def add_picture(self, slide, file_name, left, top):
        """ add picture to slide """
        slide.shapes.add_picture(
            self.file_path + file_name,
            left,
            top,
            height=self.image_display_height,
        )

    def add_title(self, slide, file_name):
        """ add title to slide """
        title = slide.placeholders[0]
        title.text = file_name
        title.text = file_name.replace(".png", "").replace(".jpg", "")

    def make_pptx(self):
        """ make powerpoint file """
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
        self.num_of_slides = len(self.files)
        for i in range(0, self.num_of_slides, self.pic_per_page):
            slide = self.presentaition.slides.add_slide(self.slide_layout)

            file_name = self.files[i]

            self.calc_aspect_ratio(file_name)
            self.calc_image_display_width()

            # センタリングする場合の画像の左上座標を計算
            left = (self.slide_width - self.image_display_width) / 2
            top = (self.slide_height - self.image_display_height) / 2

            self.add_picture(slide, file_name, left, top)
            self.add_title(slide, file_name)

        self.presentaition.save(self.output_filename)

    def make_pptx_two_or_more_pic_per_slide(self):
        self.num_of_slides = int(math.ceil(len(self.files) / self.pic_per_page))
        for i in range(0, self.num_of_slides * 2 + 3, self.pic_per_page):
            slide = self.presentaition.slides.add_slide(self.slide_layout)

            for j in range(0, self.pic_per_page):
                try:
                    file_name = self.files[i + j]
                except IndexError:
                    break

                self.calc_aspect_ratio(file_name)
                self.calc_image_display_width()

                if self.pic_per_page == 2 and j == 0:
                    # first image when paste two images to one slide
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 2 and j == 1:
                    # second image when paste two images to one slide
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 0:
                    # first image when paste three images to one slide
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 1:
                    # second image when paste three images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 3 and j == 2:
                    # third image when paste three images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 2 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 0:
                    # first image when paste four images to one slide
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 1:
                    # second image when paste four images to one slide
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 2:
                    # thrid image when paste four images to one slide
                    left = (self.slide_width / 2 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 4 and j == 3:
                    # fourth image when paste four images to one slide
                    left = (
                        (self.slide_width / 2 - self.image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 0:
                    # first image when paste six images to one slide
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 1:
                    # second image when paste six images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 2:
                    # third image when paste six images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 3:
                    # fourth image when paste six images to one slide
                    left = (self.slide_width / 3 - self.image_display_width) / 2
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 4:
                    # fifth image when paste six images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                if self.pic_per_page == 6 and j == 5:
                    # sixth image when paste six images to one slide
                    left = (
                        (self.slide_width / 3 - self.image_display_width) / 2
                    ) + self.slide_width * 2 / 3
                    top = (
                        self.slide_height - self.image_display_height
                    ) * 3 / 4 - self.pic_top_offset

                self.add_picture(slide, file_name, left, top)

                # add text
                width = height = Inches(1)
                txBox = slide.shapes.add_textbox(left, top - 400000, width, height)
                tf = txBox.text_frame
                tf.text = file_name.replace(".png", "").replace(".jpg", "")

        self.presentaition.save(self.output_filename)


pptx = PowerPoint(
    files=file_list,
    file_path=file_path,
    pic_per_page=2,
    image_height=Inches(3.0),
    # pic_top_offset=-1000000,
    pic_top_offset=0,
)
pptx.make_pptx()
