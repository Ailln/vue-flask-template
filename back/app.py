from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."


class Hello(Resource):
    @staticmethod
    def get():
        return "[get] hello flask"

    @staticmethod
    def post():
        return "[post] hello flask"


api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
