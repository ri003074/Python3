from select_dir import SelectDir
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
from pptx.enum.text import MSO_ANCHOR
from PIL import Image
from glob import glob
import wx

app = wx.App()
select_dir = SelectDir(None, title="select dir")
app.MainLoop()

# FILE_NAMES_LEFT = glob("./imgs/*.PNG")
# FILE_NAMES_CENTER = glob("./imgs2/*.PNG")
# FILE_NAMES_RIGHT = glob("./imgs/*.PNG")
FILE_NAMES_LEFT = glob(select_dir.folder1 + "/*.PNG")
FILE_NAMES_CENTER = glob(select_dir.folder2 + "/*.PNG")
FILE_NAMES_RIGHT = glob(select_dir.folder3 + "/*.PNG")
SLIDE_TITLES = ["aaa", "bbb"]
PIC_PER_PAGE = 3
IMG_DISPLAY_HEIGHT = 5  # cm
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
            file_name = FILE_NAMES_LEFT[i]
        if j == 1:
            file_name = FILE_NAMES_CENTER[i]
        if j == 2:
            file_name = FILE_NAMES_RIGHT[i]

        # 画像サイズを取得してアスペクト比を得る
        im = Image.open(file_name)
        im_width, im_height = im.size
        aspect_ratio = im_width / im_height

        # 表示された画像のサイズを計算
        img_display_height = Inches(IMG_DISPLAY_HEIGHT / 2.54)
        img_display_width = aspect_ratio * img_display_height

        if j == 0:
            # 1スライドに3枚貼り付ける場合の１枚目
            left = (SLIDE_WIDTH / 3 - img_display_width) / 2
            top = (SLIDE_HEIGHT - img_display_height) / 2

        if j == 1:
            # 1スライドに3枚貼り付ける場合の2枚目
            left = ((SLIDE_WIDTH / 3 - img_display_width) / 2) + SLIDE_WIDTH / 3
            top = (SLIDE_HEIGHT - img_display_height) / 2

        if j == 2:
            # 1スライドに3枚貼り付ける場合の3枚目
            left = ((SLIDE_WIDTH / 3 - img_display_width) / 2) + SLIDE_WIDTH * 2 / 3
            top = (SLIDE_HEIGHT - img_display_height) / 2

        slide.shapes.add_picture(
            file_name, left, top, height=Inches(IMG_DISPLAY_HEIGHT / 2.54)
        )

        # テキストを追加
        height_cm = 1
        height = Inches(height_cm / 2.54)
        width = img_display_width
        txBox = slide.shapes.add_textbox(left, top - height, width, height)
        tf = txBox.text_frame
        pg = tf.paragraphs[0]
        pg.text = (
            file_name.replace(".png", "")
            .replace(".PNG", "")
            .replace(select_dir.folder1 + "/", "")
            .replace(select_dir.folder2 + "/", "")
            .replace(select_dir.folder3 + "/", "")
        )
        pg.alignment = PP_ALIGN.CENTER
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE

prs.save(OUTPUT_FILE_NAME)
