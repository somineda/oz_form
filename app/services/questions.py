from app.models import Question
from app import db

def create_question(text):
    question = Question(text=text)
    db.session.add(question)
    db.session.commit()
    return question

def get_question(question_id):
    return Question.query.get(question_id)

def get_all_questions():
    return Question.query.all()

def get_question_by_id(question_id):
    return Question.query.get(question_id)
