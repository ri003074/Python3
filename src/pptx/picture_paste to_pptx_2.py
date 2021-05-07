from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
from PIL import Image
from glob import glob

FILE_NAMES_LEFT = glob("./imgs/*.PNG")
FILE_NAMES_RIGHT = glob("./imgs2/*.PNG")
SLIDE_TITLES = ["aaa", "bbb"]
PIC_PER_PAGE = 2
IMG_DISPLAY_HEIGHT = Inches(2.0)
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
        height = Inches(1)
        width = img_display_width
        txBox = slide.shapes.add_textbox(left, top * 0.7, width, height)
        tf = txBox.text_frame
        pg = tf.paragraphs[0]
        pg.text = file_name.replace(".png", "").replace(".PNG", "")
        pg.alignment = PP_ALIGN.CENTER
        # tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        # tf.text = file_name.replace(".png", "").replace(".PNG", "")

prs.save(OUTPUT_FILE_NAME)