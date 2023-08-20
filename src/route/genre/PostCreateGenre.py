from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.genre.PostCreateGenre import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "genre",
    type=str,
    required=True,
    default="18+ Action",
)




class PostCreateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(genre:str):
        # try:

            data = NormalizeData.process(genre = genre)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        genre = args_copy["genre"]
        response = self.post_process(genre = genre)

        return jsonify(response)


api.add_resource(
    PostCreateMovie,
    "/genre/create-genre",
    endpoint="/genre/create-genre",
)
