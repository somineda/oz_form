#answers 테이블 관련 orm 함수
from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from config import db
import app.models

from app.models import Answer, Choice, Question
from app import db

# 사용자 응답 생성
def create_answer(user_id, question_id, choice_id):
    answer = Answer(
        user_id=user_id,
        question_id=question_id,
        choice_id=choice_id
    )
    db.session.add(answer)
    db.session.commit()
    return answer

# 특정 사용자 응답 전체 조회
def get_answers_by_user(user_id):
    return Answer.query.filter_by(user_id=user_id).all()

# 특정 질문에 대한 응답 조회
def get_answers_by_question(question_id):
    return Answer.query.filter_by(question_id=question_id).all()

def get_answer_statistics():
    stats = {}

    questions = Question.query.all()

    for question in questions:
        choices = Choice.query.filter_by(question_id=question.id).all()

        choice_counts = {}
        for choice in choices:
            count = Answer.query.filter_by(question_id=question.id, choice_id=choice.id).count()
            choice_counts[choice.text] = count

        stats[question.text] = choice_counts

    return stats
