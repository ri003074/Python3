from pptx import Presentation
from glob import glob

# Presentationインスタンスの作成
ppt = Presentation("sample_slide.pptx")
# 幅
width = ppt.slide_width
# 高さ
height = ppt.slide_height

# レイアウト, 6番は白紙
blank_slide_layout = ppt.slide_layouts[1]

# 画像ファイルの読み込み
fnms = glob("./pictures/*.jpg")

# ファイル毎にループ
for fnm in fnms:
    # 白紙のスライドの追加
    slide = ppt.slides.add_slide(blank_slide_layout)
    picture_placeholder = slide.placeholders[2]
    picture_placeholder.insert_picture(fnm)

    # 画像の挿入
    pic = slide.shapes.add_picture(fnm, 0, 0)

    # 中心に移動
    pic.left = int((width - pic.width) / 2)
    pic.top = int((height - pic.height) / 2)

# 名前をつけて保存
ppt.save("figure.pptx")
