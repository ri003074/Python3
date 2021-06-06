from pptx import Presentation
from pptx.util import Inches
from PIL import Image

# from glob import glob

file_path = "./imgs/"
file_names = ["sample1.PNG", "sample2.PNG"]
# file_names = glob('*.png')

IMG_DISPLAY_HEIGHT = Inches(3.5)
PIC_PER_PAGE = 2
SLIDES = 2
OUTPUT_FILE_NAME = "output.pptx"

prs = Presentation("sample.pptx")
SLIDE_WIDTH = prs.slide_width
SLIDE_HEIGHT = prs.slide_height

for i in range(0, int(SLIDES) * 2, PIC_PER_PAGE):
    blank_slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_slide_layout)

    for j in range(0, PIC_PER_PAGE):
        # 貼り付ける画像ファイル名を取得
        file_name = file_names[i + j]

        # 画像サイズを取得してアスペクト比を得る
        im = Image.open(file_path + file_name)
        im_width, im_height = im.size
        aspect_ratio = im_width / im_height

        # 表示された画像のサイズを計算
        img_display_height = IMG_DISPLAY_HEIGHT
        img_display_width = aspect_ratio * img_display_height

        if PIC_PER_PAGE == 1:
            # センタリングする場合の画像の左上座標を計算
            left = (SLIDE_WIDTH - img_display_width) / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        if PIC_PER_PAGE == 2 and j == 0:
            # 1スライドに２枚貼り付ける場合の１枚目
            left = (SLIDE_WIDTH / 2 - img_display_width) / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        if PIC_PER_PAGE == 2 and j == 1:
            # 1スライドに２枚貼り付ける場合の2枚目
            left = ((SLIDE_WIDTH / 2 - img_display_width) / 2) + SLIDE_WIDTH / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        slide.shapes.add_picture(
            file_path + file_name, left, top, height=IMG_DISPLAY_HEIGHT
        )

        # テキストを追加
        width = height = Inches(1)
        txBox = slide.shapes.add_textbox(left, top * 0.7, width, height)
        tf = txBox.text_frame

        tf.text = file_name.replace(".png", "")

prs.save(OUTPUT_FILE_NAME)
