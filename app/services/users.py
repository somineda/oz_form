

from app.models import User
from app import db
from app.models import Answer

def create_user(name, age, gender):
    user = User(name=name, age=age, gender=gender)
    db.session.add(user)
    db.session.commit()
    return user

def get_user(user_id):
    return User.query.get(user_id)

def get_all_users():
    return User.query.all()

def get_all_users_with_answers():
    users = User.query.options(
        db.joinedload(User.answers).joinedload(Answer.question),  
        db.joinedload(User.answers).joinedload(Answer.choice)     
    ).all()
    return users

