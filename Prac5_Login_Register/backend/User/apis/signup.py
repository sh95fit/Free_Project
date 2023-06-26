from flask_restx import Namespace, Resource, fields, reqparse
from flask import Blueprint, render_template, url_for, redirect, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from random import randint
from User import jwt

from werkzeug.security import generate_password_hash, check_password_hash
from User import db

from User.models.user import User as UserModel

ns = Namespace(
  'signup',
  description='회원가입 API'
)

post_parser = reqparse.RequestParser()
post_parser.add_argument('user_type', required=True, help='유저 유형')
post_parser.add_argument('username', required=True, help='유저 아이디')
post_parser.add_argument('password', required=True, help='유저 패스워드')
post_parser.add_argument('user_name', required=True, help='유저 이름')


@ns.route('', methods=['POST'])
class SignUp(Resource) :
  @ns.expect(post_parser)
  def post(self):
      args = post_parser.parse_args()
      user_type = args['user_type']
      username = args['username']
      password = args['password']
      user_name = args['user_name']

      user = UserModel.query.filter_by(user_id=username).one_or_none()

      if user is not None:
          return jsonify(message='username exist')

      hashed_password = generate_password_hash(password)

      user = UserModel(user_type=user_type, user_id=username,
                      user_name=user_name, password=hashed_password)
      db.session.add(user)
      db.session.commit()
      return make_response(jsonify(message="user created", user_id=username), 201)