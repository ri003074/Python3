from pptx import Presentation
from pptx.util import Inches
from PIL import Image
import glob


FILE_NAMES = glob.glob("./imgs/*.PNG")

IMG_DISPLAY_HEIGHT_CM = 10
IMG_DISPLAY_HEIGHT = Inches(IMG_DISPLAY_HEIGHT_CM / 2.54)
OUTPUT_FILE_NAME = "output.pptx"

prs = Presentation()
# prs = Presentation("sample_slide.pptx")

SLIDE_WIDTH = prs.slide_width
SLIDE_HEIGHT = prs.slide_height

for i in range(0, len(FILE_NAMES)):
    blank_slide_layout = prs.slide_layouts[5]
    slide = prs.slides.add_slide(blank_slide_layout)
    title_placeholder = slide.shapes.title

    # 貼り付ける画像ファイル名を取得
    file_name = FILE_NAMES[i]
    title_placeholder.text = file_name

    # 画像サイズを取得してアスペクト比を得る
    im = Image.open(file_name)
    im_width, im_height = im.size
    aspect_ratio = im_width / im_height

    # 表示された画像のサイズを計算
    img_display_height = IMG_DISPLAY_HEIGHT
    img_display_width = aspect_ratio * img_display_height

    # センタリングする場合の画像の左上座標を計算
    left = (SLIDE_WIDTH - img_display_width) / 2
    top = (SLIDE_HEIGHT - img_display_height) / 2

    slide.shapes.add_picture(file_name, left, top, height=IMG_DISPLAY_HEIGHT)


prs.save(OUTPUT_FILE_NAME)


class PicturePaste:
    def __init__(self, file_names, image_display_height_cm, output_file_name):
        self.file_names = file_names
        self.image_display_height = Inches(image_display_height_cm / 2.54)
        self.output_file_name = output_file_name
        self.prs = Presentation()
        # self.prs = Presentation("sample_slide.pptx")
        self.slide_height = self.prs.slide_height
        self.slide_width = self.prs.slide_width

        self.make_pptx()

    def make_pptx(self):
        for i in range(0, len(self.file_names)):
            blank_slide_layout = self.prs.slide_layouts[5]
            slide = self.prs.slides.add_slide(blank_slide_layout)
            title_placeholder = slide.shapes.title

            # 貼り付ける画像ファイル名を取得
            file_name = self.file_names[i]
            title_placeholder.text = file_name

            # 画像サイズを取得してアスペクト比を得る
            im = Image.open(file_name)
            im_width, im_height = im.size
            aspect_ratio = im_width / im_height

            # 表示された画像のサイズを計算
            image_display_width = aspect_ratio * self.image_display_height

            # センタリングする場合の画像の左上座標を計算
            left = (self.slide_width - image_display_width) / 2
            top = (self.slide_height - self.image_display_height) / 2

            slide.shapes.add_picture(
                file_name, left, top, height=self.image_display_height
            )

        self.prs.save(self.output_file_name)


if __name__ == "__main__":
    pp = PicturePaste(
        file_names=FILE_NAMES,
        image_display_height_cm=10,
        output_file_name="output3.pptx",
    )
