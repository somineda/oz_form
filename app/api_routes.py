from flask import Blueprint, request, jsonify
from app.services.users import create_user
from app.services.questions import create_question, get_question_by_id, get_all_questions
from app.services.choices import create_choice, get_choices_by_question
from app.services.answers import create_answer
from app.services.images import create_image
from app.models import Choice

api_bp = Blueprint('api', __name__)

# 1. 기본 연결 확인
@api_bp.route('/', methods=['GET'])
def check_connection():
    return jsonify({"message": "Success Connect"}), 200

# 2. 메인 이미지 가져오기 (샘플 URL로)
@api_bp.route('/image/main', methods=['GET'])
def get_main_image():
    return jsonify({"image": "https://example.com/image.jpg"}), 200

# 3. 회원가입
@api_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    gender = data.get("gender")

    # 중복 체크 생략 (간단하게 처리)
    user = create_user(name=name, age=age, gender=gender)
    return jsonify({"message": f"{name}\uB2D8 \uD68C\uC6D0\uAC00\uC785\uC744 \uCD95\uD558\uD569\uB2C8\uB2E4", "user_id": user.id}), 200

# 4.1 특정 질문 가져오기
@api_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question_detail(question_id):
    q = get_question_by_id(question_id)
    if not q:
        return jsonify({"message": "\uD574\uB2F9 \uC9C8\uBB38\uC774 \uC874\uC7AC\uD558\uC9C0 \uC54A\uC2B5\uB2C8\uB2E4."}), 404
    choices = get_choices_by_question(question_id)
    return jsonify({
        "id": q.id,
        "title": q.text,
        "image": "",
        "choices": [{"id": c.id, "content": c.text, "is_active": True} for c in choices]
    }), 200

# 4.2 질문 개수
@api_bp.route('/questions/count', methods=['GET'])
def count_questions():
    total = len(get_all_questions())
    return jsonify({"total": total}), 200

# 5. 선택지 가져오기
@api_bp.route('/choice/<int:question_id>', methods=['GET'])
def get_choice_list(question_id):
    choices = get_choices_by_question(question_id)
    return jsonify({
        "choices": [{"id": c.id, "content": c.text, "is_active": True} for c in choices]
    }), 200

# 6. 답변 제출
@api_bp.route('/submit', methods=['POST'])
def submit_answers():
    data = request.get_json()
    for item in data:
        user_id = item["user_id"]
        choice_id = item["choice_id"]

        # 🔥 choice_id로부터 question_id 찾아오기
        choice = Choice.query.get(choice_id)
        if not choice:
            return jsonify({"error": "Invalid choice_id"}), 400
        question_id = choice.question_id

        create_answer(user_id=user_id, question_id=question_id, choice_id=choice_id)
        
    return jsonify({"message": f"User: {data[0]['user_id']}'s answers Success Create"}), 200

# 7.1 이미지 생성
@api_bp.route('/image', methods=['POST'])
def upload_image():
    image = create_image(user_id=1, image_url="https://example.com/image.jpg")
    return jsonify({"message": f"ID: {image.id} Image Success Create"}), 200

# 7.2 질문 생성
@api_bp.route('/question', methods=['POST'])
def upload_question():
    data = request.get_json()
    q = create_question(data.get("title"))
    return jsonify({"message": f"Title: {q.text} question Success Create"}), 200

# 7.3 선택지 생성
@api_bp.route('/choice', methods=['POST'])
def upload_choice():
    data = request.get_json()
    c = create_choice(data.get("question_id"), data.get("content"), data.get("score"))
    return jsonify({"message": f"Content: {c.text} choice Success Create"}), 200
