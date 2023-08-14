from app import api
from flask import jsonify
from flask_restx import Resource, reqparse

parser = reqparse.RequestParser()

parser.add_argument(
    "name",
    type=str,
    required=True,
    default="rnd",
)


class PostCreateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(name: str):
        # try:

        return 'create'

    # except:
    #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        name = args_copy["name"]
        response = self.post_process(name=name)

        return jsonify(response)


api.add_resource(
    PostCreateMovie,
    "/movie/create-movie",
    endpoint="/movie/create-movie",
)
