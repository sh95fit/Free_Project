from flask import Blueprint
from flask_restx import Api

from .test import ns as TestNameSpace
from .signup import ns as SignUpNameSpace
from .login import ns as LoginNameSpace

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

api = Api(
    blueprint,
    title='User Authentication API',
    doc='/docs',
    description="Welcome Hun's API docs"
)


# Add Namespace
api.add_namespace(TestNameSpace)
api.add_namespace(SignUpNameSpace)
api.add_namespace(LoginNameSpace)
