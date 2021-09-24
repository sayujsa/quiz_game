from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    new_question = Question(x['question'], x['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

for x in question_bank:
    if quiz.display_question(x):
        quiz.user_score += 1
        print(f"Correct! Your score is {quiz.user_score}/{question_bank.index(x) + 1}\n")
        quiz.question_number += 1
    else:
        print(f"Wrong Answer! Your score is {quiz.user_score}/{question_bank.index(x) + 1}\n")

print(f"Your Final Score is {quiz.user_score}/{question_bank.index(x) + 1}")

