from datetime import datetime
from zoneinfo import ZoneInfo

from config import db

# 사용자 테이블
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    email = db.Column(db.String(100))

    answers = db.relationship('Answer', back_populates='user', lazy=True)
    images = db.relationship('Image', back_populates='user', lazy=True)

# 이미지 테이블
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_url = db.Column(db.String(255))

    user = db.relationship('User', back_populates='images')

# 질문 테이블
class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    choices = db.relationship('Choice', back_populates='question', lazy=True)
    answers = db.relationship('Answer', back_populates='question', lazy=True)

# 보기/선택지 테이블
class Choice(db.Model):
    __tablename__ = 'choices'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))

    question = db.relationship('Question', back_populates='choices')
    answers = db.relationship('Answer', back_populates='choice', lazy=True)

# 사용자의 답변 테이블
class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choices.id'), nullable=False)

    user = db.relationship('User', back_populates='answers')
    question = db.relationship('Question', back_populates='answers')
    choice = db.relationship('Choice', back_populates='answers')
