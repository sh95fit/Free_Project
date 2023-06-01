from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin


def create_app():
    print('run create app()')
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return 'hello world!!!'

    # @app.route('/test')
    # @cross_origin()
    # def test():
    #     data = {
    #         "member": [
    #             {"id": 1, "test": "good"},
    #             {"id": 2, "Let": "develop"}
    #         ]
    #     }
    #     return jsonify(data)

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    return app
