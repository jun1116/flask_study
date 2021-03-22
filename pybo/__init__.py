#-*-coding:utf-8-*-
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # config.py 에 작성한 항목을 app.config 환경변수로 부르기 위해 추가한 코드

    #ORM
    db.init_app(app) #초기화
    migrate.init_app(app, db) #초기화
    #model
    from . import models

    
    # Blue Print
    from .views import main_views
    from .views import question_view
    from .views import answer_view
    
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_view.bp)
    app.register_blueprint(answer_view.bp)

    # @app.route('/')
    # def hello_pybo():
    #     return render_template('index.html')

    return app

# if __name__=='__main__':
#     app = create_app()
#     app.run(debug=True)