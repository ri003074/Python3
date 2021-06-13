# import sys

# abc = ["abc", "def", "ghi"]

# dic = {"abc": "AAA", "def": "DDD"}


# for i in range(len(abc)):
#     for key, value in dic.items():
#         if abc[i] == key:
#             abc[i] = value

# print(abc)


# class Outer:
#     def __init__(self):
#         print("create Outer Class")
#         print(self.Inner)
#         # self.Innerのメモリサイズを確認
#         print(sys.getsizeof(self.Inner))
#         self.inner = self.Inner()
#         print(self.inner)

#     class Inner:
#         def __init__(self):
#             print("create Inner Class")

#         def abc(self):
#             print("inner abc")


# outer = Outer()

# outer.inner.abc()

# from pptx import Presentation
# from pptx.util import Inches, Pt, Cm
# from pptx.enum.text import PP_ALIGN


# prs = Presentation()
# blank_slide_layout = prs.slide_layouts[6]
# slide = prs.slides.add_slide(blank_slide_layout)

# left = Cm(3)
# top = Cm(2.5)
# width = Cm(15)
# height = Cm(1)
# txBox = slide.shapes.add_textbox(left, top, width, height)
# tf = txBox.text_frame
# tf.text = "Hello"
# txBox.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

# p = tf.add_paragraph()
# p.alignment = PP_ALIGN.CENTER
# run = p.add_run()
# run.text = "Just an example"
# font = run.font


# prs.save("test.pptx")


# def test(*file_list):
#     print(file_list)
#     for (file1, file2) in zip(file_list):
#         print(file1)


# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# test(lst1, lst2)


# from pptx.util import Inches, Pt, Cm

# print(Pt(1) * 72)
# print(Inches(1))
# print(Pt(10))
# print(Pt(28.34))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]

# for (a, b) in zip(lst1, lst2):
#     print(a)
#     print(b)


class A:
    def __init__(self, moji):
        self.str = moji

    def add(self, moji):
        self.str = self.str + moji

    def show(self):
        print(self.str)


a = A("abc")
a.add("def")
a.show()


print(a)


lst = [1, 2, 3]
print(sum(lst))
