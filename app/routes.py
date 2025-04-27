from flask import Blueprint, render_template, request, redirect, url_for, session
from app.services.users import get_all_users_with_answers
from app.services.answers import get_answer_statistics
from app.services.result_service import get_answer_statistics

main_bp = Blueprint('main', __name__)

# 홈 화면
@main_bp.route('/')
def index():
    return render_template('index.html')

#시작
@main_bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # 설문 결과 저장 로직 들어갈 자리
        return redirect(url_for('main.results'))
    return render_template('quiz.html')


# 관리자 로그인
@main_bp.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # 로그인 처리 로직
        return redirect(url_for('main.admin_dashboard'))
    return render_template('admin_login.html')

# 관리자 대시보드
@main_bp.route('/admin/dashboard')
def admin_dashboard():
    users = get_all_users_with_answers()  # 유저 + 응답 불러오기
    return render_template('admin_dashboard.html', users=users)

@main_bp.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz_step(question_id):
    import requests

    if request.method == 'POST':
        api_url = request.form.get('api_url')
        user_id = request.form.get('user_id')
        choice_id = request.form.get('choice_id')

        # 응답 저장
        requests.post(f"{api_url}/api/submit", json=[{
            "user_id": int(user_id),
            "choice_id": int(choice_id)
        }])

        next_question = question_id + 1
        total = requests.get(f"{api_url}/api/questions/count").json().get("total")
        if next_question > total:
            return redirect(url_for('main.results_view'))

        return redirect(url_for('main.quiz_step', user_id=user_id, api_url=api_url, question_id=next_question))

    else:
        api_url = request.args.get('api_url')
        user_id = request.args.get('user_id')
        q = requests.get(f"{api_url}/api/questions/{question_id}").json()

        return render_template('question.html', question=q, api_url=api_url, user_id=user_id)
    
@main_bp.route('/signup', methods=['POST'])
def signup_api():
    import requests
    api_url = request.form.get('api_url')
    user_data = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "gender": request.form.get('gender'),
        "age": int(request.form.get('age'))
    }

    try:
        res = requests.post(f"{api_url}/api/signup", json=user_data)
        if res.status_code == 200:
            user_id = res.json().get("user_id")
            return redirect(url_for('main.quiz_step', user_id=user_id, api_url=api_url, question_id=1))
        else:
            return "회원가입 실패", 400
    except Exception:
        return "회원가입 중 오류 발생", 500
@main_bp.route('/connect', methods=['POST'])
def connect():
    api_url = request.form.get('api_url')
    
    import requests
    try:
        res = requests.get(f"{api_url}/api/")
        if res.status_code == 200 and res.json().get("message") == "Success Connect":
            return render_template('signup.html', api_url=api_url)
        else:
            return "API 연결 실패", 400
    except Exception:
        return "API 요청 중 오류 발생", 500

@main_bp.route('/admin/dashboard')
def admin_dashboard_view():
    users = get_all_users_with_answers()
    return render_template('admin_dashboard.html', users=users)

@main_bp.route('/results')
def results_view():
    stats = get_answer_statistics()
    return render_template('results.html', stats=stats)

