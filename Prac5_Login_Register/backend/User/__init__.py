from flask import Flask, render_template, jsonify
# from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from User import info

import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from datetime import timedelta

jwt = JWTManager()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    print('run create app()')
    app = Flask(__name__)
    load_dotenv()
    # CORS(app)

    """디버깅 모드에서 캐시 제거"""
    if app.config['DEBUG'] == True:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
        app.config['TEMPLATES_AUTO_RELOAD'] = True


    """ === Routes Init === """
    from .routes import auth_route
    app.register_blueprint(auth_route.bp)

    '''DB INIT (sqlite의 경우 배치로 처리)'''
    # app.config['SQLALCHEMY_DATABASE_URI'] = info.db_uri
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('db_uri')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    '''Restx Init'''
    from .apis import blueprint as api
    app.register_blueprint(api)
    # 세부 내용을 리스트 형태로 표시 (앤드포인트에 대한 요약정보만 펼쳐서 표시)
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

    '''JWT Init'''
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = "7 day"
    jwt.init_app(app)


    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    return app
