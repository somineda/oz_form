
#개발환경에서 테스트 하는 실행 파일



from app import create_app, db  
from flask_migrate import Migrate  

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)

    

