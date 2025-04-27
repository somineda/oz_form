from app.models import Answer, Question, Choice
from config import db

def get_answer_statistics():
    stats = {}
    questions = Question.query.all()

    for question in questions:
        choices_count = {}
        for choice in question.choices:
            count = Answer.query.filter_by(choice_id=choice.id).count()
            choices_count[choice.text] = count
        stats[question.text] = choices_count

    return stats
