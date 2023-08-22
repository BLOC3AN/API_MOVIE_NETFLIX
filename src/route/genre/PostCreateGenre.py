from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.genre.PostCreateGenre import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "genres",
    type=str,
    required=True,
    default="18+ Action",
)




class PostCreateGenre(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(genres:str):
        # try:

            data = NormalizeData.process(genres = genres)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        genres = args_copy["genres"]
        response = self.post_process(genres = genres)

        return jsonify(response)


api.add_resource(
    PostCreateGenre,
    "/genre/create-genre",
    endpoint="/genre/create-genre",
)
