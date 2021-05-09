from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
from pptx.enum.text import MSO_ANCHOR
from PIL import Image
from glob import glob

FILE_NAMES_LEFT = glob("./imgs/*.PNG")
FILE_NAMES_RIGHT = glob("./imgs2/*.PNG")
SLIDE_TITLES = ["aaa", "bbb"]
PIC_PER_PAGE = 2
IMG_DISPLAY_HEIGHT_CM = 5
IMG_DISPLAY_HEIGHT = Inches(IMG_DISPLAY_HEIGHT_CM / 2.54)
SLIDE_COUNT = len(SLIDE_TITLES)

# prs = Presentation("sample_slide.pptx")
prs = Presentation()
SLIDE_WIDTH = prs.slide_width
SLIDE_HEIGHT = prs.slide_height
OUTPUT_FILE_NAME = "output.pptx"
SLIDE_LAYOUT = prs.slide_layouts[5]

for i in range(0, SLIDE_COUNT):
    slide = prs.slides.add_slide(SLIDE_LAYOUT)
    title_placeholder = slide.shapes.title
    title_placeholder.text = SLIDE_TITLES[i]

    for j in range(0, PIC_PER_PAGE):
        if j == 0:
            # 貼り付ける画像ファイル名を取得
            file_name = FILE_NAMES_LEFT[i]
        if j == 1:
            # 貼り付ける画像ファイル名を取得
            file_name = FILE_NAMES_RIGHT[i]

        # 画像サイズを取得してアスペクト比を得る
        im = Image.open(file_name)
        im_width, im_height = im.size
        aspect_ratio = im_width / im_height

        # 表示された画像のサイズを計算
        img_display_height = IMG_DISPLAY_HEIGHT
        img_display_width = aspect_ratio * img_display_height

        if j == 0:
            # 1スライドに２枚貼り付ける場合の１枚目
            left = (SLIDE_WIDTH / 2 - img_display_width) / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        if j == 1:
            # 1スライドに２枚貼り付ける場合の2枚目
            left = ((SLIDE_WIDTH / 2 - img_display_width) / 2) + SLIDE_WIDTH / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        slide.shapes.add_picture(file_name, left, top, height=IMG_DISPLAY_HEIGHT)

        # テキストを追加
        height_cm = 1
        height = Inches(height_cm / 2.54)
        width = img_display_width
        txBox = slide.shapes.add_textbox(left, top - height, width, height)
        tf = txBox.text_frame
        pg = tf.paragraphs[0]
        pg.text = file_name.replace(".png", "").replace(".PNG", "")
        pg.alignment = PP_ALIGN.CENTER
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        # tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        # tf.text = file_name.replace(".png", "").replace(".PNG", "")

prs.save(OUTPUT_FILE_NAME)


class PicturePaste:
    def __init__(
        self,
        file_names_left,
        file_names_right,
        slide_titles,
        image_display_height_cm,
        output_file_name,
    ):
        self.file_names_left = file_names_left
        self.file_names_right = file_names_right
        self.slide_titles = slide_titles
        self.image_display_height = Inches(image_display_height_cm / 2.54)
        self.output_file_name = output_file_name

        self.prs = Presentation()
        # self.prs = Presentation("sample_slide.pptx")
        self.slide_height = self.prs.slide_height
        self.slide_width = self.prs.slide_width
        self.slide_layout = self.prs.slide_layouts[5]
        self.pic_per_page = 2

        self.make_pptx()

    def make_pptx(self):
        for i in range(0, len(self.file_names_left)):
            slide = self.prs.slides.add_slide(self.slide_layout)
            title_placeholder = slide.shapes.title
            title_placeholder.text = self.slide_titles[i]

            for j in range(0, self.pic_per_page):
                if j == 0:
                    # 貼り付ける画像ファイル名を取得
                    file_name = self.file_names_left[i]
                if j == 1:
                    # 貼り付ける画像ファイル名を取得
                    file_name = self.file_names_right[i]

                # 画像サイズを取得してアスペクト比を得る
                im = Image.open(file_name)
                im_width, im_height = im.size
                aspect_ratio = im_width / im_height

                # 表示された画像のサイズを計算
                image_display_width = aspect_ratio * self.image_display_height

                if j == 0:
                    # 1スライドに２枚貼り付ける場合の１枚目
                    left = (self.slide_width / 2 - image_display_width) / 2
                    top = (self.slide_height - self.image_display_height) / 2

                if j == 1:
                    # 1スライドに２枚貼り付ける場合の2枚目
                    left = (
                        (self.slide_width / 2 - image_display_width) / 2
                    ) + self.slide_width / 2
                    top = (self.slide_height - self.image_display_height) / 2

                slide.shapes.add_picture(
                    file_name, left, top, height=self.image_display_height
                )

                # テキストを追加
                height_cm = 1
                height = Inches(height_cm / 2.54)
                width = image_display_width
                txBox = slide.shapes.add_textbox(left, top - height, width, height)
                tf = txBox.text_frame
                pg = tf.paragraphs[0]
                pg.text = file_name.replace(".png", "").replace(".PNG", "")
                pg.alignment = PP_ALIGN.CENTER
                tf.vertical_anchor = MSO_ANCHOR.MIDDLE
                # tf.paragraphs[0].alignment = PP_ALIGN.CENTER
                # tf.text = file_name.replace(".png", "").replace(".PNG", "")

        self.prs.save(self.output_file_name)


if __name__ == "__main__":
    FILE_NAMES_LEFT = glob("./imgs/*.PNG")
    FILE_NAMES_RIGHT = glob("./imgs2/*.PNG")
    SLIDE_TITLES = ["aaa", "bbb"]
    pp = PicturePaste(
        file_names_left=FILE_NAMES_LEFT,
        file_names_right=FILE_NAMES_RIGHT,
        slide_titles=SLIDE_TITLES,
        image_display_height_cm=5,
        output_file_name="output4.pptx",
    )
