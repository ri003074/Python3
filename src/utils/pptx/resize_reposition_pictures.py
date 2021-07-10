import win32com.client
import math
import sys

# from icecream import ic
import dataclasses
import easygui
import re


@dataclasses.dataclass
class ShapeData:
    Type: int = 0
    Top: int = 0
    Left: int = 0
    Width: int = 0
    Height: int = 0


pptx = win32com.client.Dispatch("PowerPoint.Application")
active_presentation = pptx.ActivePresentation
slide_count = active_presentation.Slides.Count

answer = easygui.ynbox(f"Are you sure want to fix {active_presentation.FullName}?")
if answer is False:
    sys.exit()

reference_slide_number = easygui.enterbox("input reference slide number")
fix_slide_number = easygui.enterbox(
    "input fix slide number. Input format is 1,3,5 or 1~3 or all"
)

if "~" in fix_slide_number:
    match_number = re.match("(\\d*)~(\\d*)", fix_slide_number)
    fix_slide_list = list(
        range(int(match_number.group(1)), int(match_number.group(2)) + 1)
    )
elif "all" in fix_slide_number:
    fix_slide_list = list(range(1, slide_count + 1))
else:
    s = fix_slide_number.replace(",", "")
    fix_slide_list = [int(i) for i in s]


# make reference data
reference_slide_number = int(reference_slide_number)
reference_data_list = []
shapes_per_slide = active_presentation.Slides(reference_slide_number).Shapes.Count

for shape_index in range(1, shapes_per_slide + 1):
    reference_shape = active_presentation.Slides(reference_slide_number).Shapes(
        shape_index
    )
    reference_data_object = ShapeData()
    reference_data_object.Type = reference_shape.Type
    reference_data_object.Top = reference_shape.Top
    reference_data_object.Left = reference_shape.Left
    reference_data_object.Width = reference_shape.Width
    reference_data_object.Height = reference_shape.Height
    reference_data_list.append(reference_data_object)


# start resize and reposition
resize_slide_target = fix_slide_list
for slide_number in resize_slide_target:
    shapes_per_slide = active_presentation.Slides(slide_number).Shapes.Count
    for shape_index in range(1, shapes_per_slide + 1):
        target_shape = active_presentation.Slides(slide_number).Shapes(shape_index)
        distance_list = []
        for reference_data in reference_data_list:
            distance = math.sqrt(
                (reference_data.Top - target_shape.Top) ** 2
                + (reference_data.Left - target_shape.Left) ** 2
            )
            # ic(distance)
            distance_list.append(distance)

        min_value = min(distance_list)
        min_index = distance_list.index(min_value)
        target_shape.Top = reference_data_list[min_index].Top
        target_shape.Left = reference_data_list[min_index].Left
        target_shape.Width = reference_data_list[min_index].Width
        target_shape.Height = reference_data_list[min_index].Height
