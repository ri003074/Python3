if __name__ == "__main__":
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     print(type(line))
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    # data = student_marks[query_name]
    data = (1.0, 1.0)
    print(sum(data) / len(data))
    print(f"{(sum(data) / len(data)):.02f}")
