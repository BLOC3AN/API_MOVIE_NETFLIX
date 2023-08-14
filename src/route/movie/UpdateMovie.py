from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.movie.UpdateMovie import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "id",
    type=str,
    required=True,
    default="",
)

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


class UpdateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def put_process(id: str,name: str, genre:str, cast: str):
        # try:

            data = NormalizeData.process(id=id, name=name, genre=genre, cast=cast)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def put(self):
        args = parser.parse_args()
        args_copy = args.copy()
        id= args_copy["id"]
        name = args_copy["name"]
        genre = args_copy["genre"]
        cast = args_copy["cast"]

        response = self.put_process(id=id,name=name,genre=genre, cast=cast)

        return jsonify(response)


api.add_resource(
    UpdateMovie,
    "/movie/update-movie",
    endpoint="/movie/update-movie",
)
