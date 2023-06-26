from flask_restx import Namespace, Resource
from flask import jsonify, Blueprint, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
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
    user_id = get_jwt_identity()
    return make_response(jsonify(message="success", user_id=user_id),200)
    # return {"message" : "success"}, 200