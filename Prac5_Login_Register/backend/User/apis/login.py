from flask_restx import Namespace, Resource, fields, reqparse
from flask import Blueprint, render_template, url_for, redirect, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from random import randint
from User import jwt

from werkzeug.security import generate_password_hash, check_password_hash
from User import db

from User.models.user import User as UserModel

ns = Namespace(
  'login',
  description='회원가입 API'
)

post_parse =  reqparse.RequestParser()
post_parse.add_argument('username', required=True, help='유저 아이디')
post_parse.add_argument('password', required=True, help='유저 패스워드')

@ns.route('', methods=['POST'])
class Login(Resource) :
  @ns.expect(post_parse)
  def post(self):
      args = post_parse.parse_args()
      username = args["username"]
      password = args["password"]

      user = UserModel.query.filter_by(user_id=username).one_or_none()

      if user is not None and check_password_hash(user.password, password):
          access_token = create_access_token(identity=username)
          response = jsonify(message='success', access_token=access_token)
          return make_response(response, 200)
      else:
          return make_response(jsonify(message='login failed'), 401)