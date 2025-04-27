from app import db
from app.models import Question, Choice

def seed_data():
    # 질문 1
    q1 = Question(text="평소에 프로야구 관람을 하시나요?")
    db.session.add(q1)
    db.session.flush()  

    db.session.add_all([
        Choice(question_id=q1.id, text="예"),
        Choice(question_id=q1.id, text="아니오")
    ])

    # 질문 2
    q2 = Question(text="관람을 하신다면 주로 어느 루트로 관람하시나요?")
    db.session.add(q2)
    db.session.flush()

    db.session.add_all([
        Choice(question_id=q2.id, text="TV 중계"),
        Choice(question_id=q2.id, text="티빙"),
        Choice(question_id=q2.id, text="직관")
    ])

    # 질문 3
    q3 = Question(text="어떤 KBO 팀을 응원하시나요?")
    db.session.add(q3)
    db.session.flush()

    db.session.add_all([
        Choice(question_id=q3.id, text="LG"),
        Choice(question_id=q3.id, text="삼성"),
        Choice(question_id=q3.id, text="KIA"),
        Choice(question_id=q3.id, text="키움"),
        Choice(question_id=q3.id, text="롯데"),
        Choice(question_id=q3.id, text="두산"),
        Choice(question_id=q3.id, text="한화"),
        Choice(question_id=q3.id, text="KT"),
        Choice(question_id=q3.id, text="SSG"),
        Choice(question_id=q3.id, text="NC"),
    ])

    # 질문 4
    q4 = Question(text="올해 어떤 KBO 팀이 우승할 것 같나요?")
    db.session.add(q4)
    db.session.flush()

    db.session.add_all([
        Choice(question_id=q4.id, text="LG"),
        Choice(question_id=q4.id, text="삼성"),
        Choice(question_id=q4.id, text="KIA"),
        Choice(question_id=q4.id, text="키움"),
        Choice(question_id=q4.id, text="롯데"),
        Choice(question_id=q4.id, text="두산"),
        Choice(question_id=q4.id, text="한화"),
        Choice(question_id=q4.id, text="KT"),
        Choice(question_id=q4.id, text="SSG"),
        Choice(question_id=q4.id, text="NC"),
    ])

    db.session.commit()
    print("✅ 더미 질문과 보기 데이터가 성공적으로 입력되었습니다.")

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    app.app_context().push()
    seed_data()
