from app import create_app, db
from app.seeds import seed_data

# 앱 생성
app = create_app()

# 앱 컨텍스트 안에서 실행
with app.app_context():
    seed_data()
