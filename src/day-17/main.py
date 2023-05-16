from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [Question(question["question"], question['correct_answer'])
                 for question in question_data]


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f'You final score was {quiz.score}/ {quiz.questions_length}')
