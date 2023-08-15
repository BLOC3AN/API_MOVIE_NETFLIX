from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.movie.PostCreateMovie import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "name",
    type=str,
    required=True,
    default="Sieu anh hung",
)

parser.add_argument(
    "genre",
    type=str,
    required=True,
    default='Khong xac dinh'
)

parser.add_argument(
    "cast",
    type=str,
    required=True,
    default="Chi Dan"
)


class PostCreateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(name: str, genre:str, cast: str):
        # try:

            data = NormalizeData.process(name=name, genre=genre, cast=cast)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        name = args_copy["name"]
        genre = args_copy["genre"]
        cast = args_copy["cast"]

        response = self.post_process(name=name,genre=genre, cast=cast)

        return jsonify(response)


api.add_resource(
    PostCreateMovie,
    "/movie/create-movie",
    endpoint="/movie/create-movie",
)
