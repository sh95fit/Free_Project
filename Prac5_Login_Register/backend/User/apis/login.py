from flask_restx import Namespace, Resource
from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from random import randint
from User import jwt

ns = Namespace(
  'login',
  description='JWT 방식 로그인 API'
)


@ns.route('', methods=['GET'])
class Login(Resource) :
  @jwt_required()
  def generate() :
    return jsonify(message='success'), 200