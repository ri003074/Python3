from pptx import Presentation
from pptx.util import Inches
from PIL import Image
from glob import glob

file_names_left = glob("./imgs/*.png")
file_names_right = glob("./imgs2/*.png")
slide_titles = ["aaa", "bbb"]

IMG_DISPLAY_HEIGHT = Inches(2.0)
PIC_PER_PAGE = 2
SLIDE_COUNT = len(file_names_left)
OUTPUT_FILE_NAME = "output.pptx"

# prs = Presentation("sample_slide.pptx")
prs = Presentation()
SLIDE_WIDTH = prs.slide_width
SLIDE_HEIGHT = prs.slide_height

for i in range(0, SLIDE_COUNT):
    blank_slide_layout = prs.slide_layouts[5]
    slide = prs.slides.add_slide(blank_slide_layout)
    title_placeholder = slide.shapes.title
    title_placeholder.text = slide_titles[i]

    for j in range(0, PIC_PER_PAGE):
        if j == 0:
            # 貼り付ける画像ファイル名を取得
            file_name = file_names_left[i]
        if j == 1:
            # 貼り付ける画像ファイル名を取得
            file_name = file_names_right[i]

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
        width = height = Inches(1)
        txBox = slide.shapes.add_textbox(left, top * 0.7, width, height)
        tf = txBox.text_frame

        tf.text = file_name.replace(".png", "").replace(".PNG", "")

prs.save(OUTPUT_FILE_NAME)
