from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.actor.UpdateActor import NormalizeData

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
    default="MARIA OZAWA",
)

parser.add_argument(
    "born",
    type=str,
    required=True,
    default="1986",
)

parser.add_argument(
    "country",
    type=str,
    required=True,
    default="japanese",
)

parser.add_argument(
    "film",
    type=str,
    required=True,
    default="Tho sua ong nuoc may man, Co thu ky",
)

class UpdateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def put_process(id: str,name: str, country: str, film: str):
        # try:

            data = NormalizeData.process(id=id, name=name, country=country, film=film )

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def put(self):
        args = parser.parse_args()
        args_copy = args.copy()
        id= args_copy["id"]
        name = args_copy["name"]
        country = args_copy["country"]
        film = args_copy["film"]

        response = self.put_process(id=id, name=name, country=country, film=film)

        return jsonify(response)


api.add_resource(
    UpdateMovie,
    "/movie/update-actor",
    endpoint="/movie/update-actor",
)
