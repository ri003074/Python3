class Student(object):
    def __init__(self, firstName, lastName, idNumber, score):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = score

    def printPerson(self):
        print(f"Name: {self.lastName}, {self.firstName}")
        print(f"ID:{self.idNumber}")

    def calculator(self):
        sum = 0
        score_num = len(self.scores)
        for i in range(score_num):
            sum += self.scores[i]

        avg = sum / score_num

        grade = ""
        if avg >= 90:
            grade = "O"
        elif avg >= 80:
            grade = "E"
        elif avg >= 70:
            grade = "E"
        elif avg >= 55:
            grade = "E"
        elif avg >= 40:
            grade = "E"
        else:
            grade = "T"

        return grade


him = Student("kenta", "kawamoto", 1111, (100, 50, 70, 60, 80, 60))

print(him.printPerson())
print(him.calculator())
