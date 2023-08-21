from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.movie.GetMovie import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "id",
    type=str,
    required=True,
    default="",
)


class GetMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def put_process(id: str):
        # try:

            data = NormalizeData.process(id=id)
            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def put(self):
        args = parser.parse_args()
        args_copy = args.copy()
        id= args_copy["id"]

        response = self.put_process(id=id)

        return jsonify(response)


api.add_resource(
    GetMovie,
    "/movie/get-movie",
    endpoint="/movie/get-movie",
)
