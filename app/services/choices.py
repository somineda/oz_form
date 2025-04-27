
from config import db
from flask import abort

from app.models import Choice


def create_choice(question_id, text, score=0):
    choice = Choice(question_id=question_id, text=text, score=score)
    db.session.add(choice)
    db.session.commit()
    return choice

def get_choices_by_question(question_id):
    return Choice.query.filter_by(question_id=question_id).all()
