from flask import Blueprint, render_template, url_for, redirect, jsonify
from User.models.user import User as UserModel

NAME = 'auth'

bp = Blueprint(NAME, __name__, url_prefix='/auth')


@bp.route('/')
def index():
    return "Login, Register"


# @bp.route('/test')
# def test():
#     data = {
#         "member": [
#             {"id": 1, "test": "good"},
#             {"id": 2, "Let": "develop"}
#         ]
#     }
#     return jsonify(data)
