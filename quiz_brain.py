class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 1
        self.user_score = 0
        self.question_list = question_list

    def display_question(self, question_object):
        y_or_n = input(f"Q.{self.question_number} - {question_object.question_text} (true/false) : ").lower()
        if y_or_n == question_object.answer:
            return True
        else:
            return False
