from flask_restx import Namespace, Resource
from flask import jsonify, Blueprint, make_response
from flask_jwt_extended import jwt_required
from random import randint
from User import jwt

ns = Namespace(
  'test',
  description='JWT 방식 로그인 API'
)


@ns.route('', methods=['GET'])
class Test(Resource) :
  @jwt_required()
  def get(self) :
    return make_response(jsonify(message="success"),200)
    # return {"message" : "success"}, 200