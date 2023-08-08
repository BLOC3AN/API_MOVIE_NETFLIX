
import os
from flask import Flask
from flask_restx import Api
from flask_cors import CORS

# init config
def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    return app

app = create_app()
app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app, version='1.0', title='API Movies Gateway',
          description='API Movies Gateway documentation',)

# Please give import route in here
from src.route.index import *

if __name__ == "__main__":
    # from argparse import ArgumentParser
    # parser = ArgumentParser()
    # parser.add_argument('-p', '--port', default=18707,
    #                     type=int, help='port to listen on')
    # args = parser.parse_args()
    # # print(f"args: {args}")
    # port = args.port
    # app.run(host='0.0.0.0', port=port, debug=os.environ.get("IS_DEBUG", False))

    app.run(host='localhost', port=5001, debug=True)
