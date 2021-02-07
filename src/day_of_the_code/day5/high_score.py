student_scores = [78, 86, 91]

max = 0
for score in student_scores:
    if max < score:
        max = score

print(max)
