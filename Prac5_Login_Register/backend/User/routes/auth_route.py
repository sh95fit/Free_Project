from flask import Blueprint, render_template, url_for, redirect, jsonify, request
from User.models.user import User as UserModel
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from User import db

NAME = 'auth'

bp = Blueprint(NAME, __name__, url_prefix='/auth')


@bp.route('/')
def index():
    return "Login, Register"


@bp.route('/test')
def test():
    data = {
        "member": [
            {"id": 1, "test": "good"},
            {"id": 2, "Let": "develop"}
        ]
    }
    return jsonify(data)


@bp.route('/register', methods=['POST'])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    user = UserModel.query.filter_by(user_id=username).one_or_none()

    if user is not None:
        return jsonify(message='username exist')

    hashed_password = generate_password_hash(password)

    user = UserModel(user_type=1, user_id=username,
                     user_name='test', password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message='user created')


@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = UserModel.query.filter_by(user_id=username).one_or_none()

    if user is not None and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        response = jsonify(message='success', access_token=access_token)
        return response, 200
    else:
        return jsonify(message='login failed'), 401
