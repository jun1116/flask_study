from flask import Flask, render_template, request,redirect,send_file
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)


    #ORM
    app.config.from_object(config) # config.py 에 작성한 항목을 app.config 환경변수로 부르기 위해 추가한 코드

    db.init_app(app) #초기화
    migrate.init_app(app, db) #초기화

    # Blue Print
    from .views import main_views
    app.register_blueprint(main_views.bp)

    @app.route('/')
    def hello_pybo():
        return 'HELLO PYBO'
    return app

