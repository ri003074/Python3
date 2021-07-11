from pptx import Presentation
from pptx.util import Inches, Pt
from PIL import Image
import glob
import easygui
import os
import datetime
from pptx.dml.color import RGBColor

# C:\Users\ri003\Documents\Programming\Python3\src\utils\pptx>pyinstaller "gui_picture_paste to_pptx.py" --onefile --additional-hooks-dir hook
""" hook-pptx.py

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files("pptx")

"""


class PicturePaste:
    def __init__(
        self, file_names, image_display_height_cm, title_font_size_pt, output_file_name
    ):
        self.file_names = file_names
        self.image_display_height = Inches(image_display_height_cm / 2.54)
        self.output_file_name = output_file_name
        self.prs = Presentation()
        # self.prs = Presentation("sample_slide.pptx")
        self.slide_height = self.prs.slide_height
        self.slide_width = self.prs.slide_width
        self.title_font_size_pt = title_font_size_pt

        self.make_pptx()

    def make_pptx(self):
        for i in range(0, len(self.file_names)):
            blank_slide_layout = self.prs.slide_layouts[5]
            slide = self.prs.slides.add_slide(blank_slide_layout)
            title_placeholder = slide.shapes.title

            # 貼り付ける画像ファイル名を取得
            file_path = self.file_names[i]
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            title_placeholder.text = file_name
            title_placeholder.text_frame.paragraphs[0].font.size = Pt(
                self.title_font_size_pt
            )
            title_placeholder.text_frame.paragraphs[0].font.color.rgb = RGBColor(
                0, 176, 80
            )

            # 画像サイズを取得してアスペクト比を得る
            im = Image.open(file_path)
            im_width, im_height = im.size
            aspect_ratio = im_width / im_height

            # 表示された画像のサイズを計算
            image_display_width = aspect_ratio * self.image_display_height

            # センタリングする場合の画像の左上座標を計算
            left = (self.slide_width - image_display_width) / 2
            top = (self.slide_height - self.image_display_height) / 2

            slide.shapes.add_picture(
                file_path, left, top, height=self.image_display_height
            )

        self.prs.save(self.output_file_name)


if __name__ == "__main__":
    now = datetime.datetime.now()
    date_now = now.strftime("%Y%m%d%H%M")
    image_file_path = easygui.diropenbox("input picture path")
    output_file_path = easygui.diropenbox("output file path")
    output_file_name = easygui.enterbox("input output file name")
    FILE_NAMES = glob.glob(image_file_path + "**/*.PNG", recursive=True)
    pp = PicturePaste(
        file_names=FILE_NAMES,
        image_display_height_cm=10,
        title_font_size_pt=16,
        output_file_name=output_file_path
        + "/"
        + date_now
        + "_"
        + output_file_name
        + ".pptx",
    )
