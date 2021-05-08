# from pptx import Presentation

# prs = Presentation()
# title_slide_layout = prs.slide_layouts[0]
# title_and_contents_slide_layout = prs.slide_layouts[1]


# # title layout
# slide = prs.slides.add_slide(title_slide_layout)
# # title = slide.placeholders[0]
# title = slide.shapes.title

# subtitle = slide.placeholders[1]

# title.text = "Hello, World!"
# subtitle.text = "python-pptx was here!"

# for shape in slide.shapes:
#     if shape.is_placeholder:
#         phf = shape.placeholder_format
#         print("%d, %s" % (phf.idx, phf.type))


# # title and slide layout
# slide = prs.slides.add_slide(title_and_contents_slide_layout)
# title = slide.shapes.title
# title.text = "title and slide layout"
# contents = slide.placeholders[1]
# contents.text = "contents"
# # print(contents.shape_type)

# for shape in slide.shapes:
#     if shape.is_placeholder:
#         phf = shape.placeholder_format
#         print("%d, %s" % (phf.idx, phf.type))

# prs.save("test.pptx")


from pptx import Presentation

prs = Presentation()

for i in range(0, 10):
    slide = prs.slides.add_slide(prs.slide_layouts[i])
    print(f"slide{i}")
    for shape in slide.shapes:
        if shape.is_placeholder:
            phf = shape.placeholder_format
            print(f"{phf.idx}, {phf.type}")
