from flask import Blueprint
from flask_restx import Api

from .login import ns as TestNameSpace

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
