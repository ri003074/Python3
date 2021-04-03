import pandas

student_dict = {"student": ["angela", "jun", "john"], "score": [1, 2, 3]}

student_data_frame = pandas.DataFrame(student_dict)

for index, row in student_data_frame.iterrows():
    print(row.student)
