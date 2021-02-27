from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for i in range(len(question_data)):
#     question_bank.append(
#         Question(text=question_data[i]["text"], answer=question_data[i]["answer"])
#     )


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{len(question_data)}")
