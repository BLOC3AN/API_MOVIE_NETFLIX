from app import api
from flask import jsonify
from flask_restx import Resource, reqparse
from src.common.ResponseError import response as ResponseError
from src.common.ResponseSuccess import response as ResponseSuccess

from src.handlers.actor.PostCreateActor import NormalizeData

parser = reqparse.RequestParser()

parser.add_argument(
    "name",
    type=str,
    required=True,
    default="MARIA OZAWA",
)
parser.add_argument(
    "img",
    type=str,
    required=True,
    default="https://www.google.com/url?sa=i&url=https%3A%2F%2F2sao.vn%2Fmaria-ozawa-bi-coi-re-di-biet-xu-khong-ai-thuc-su-yeu-thuong-n-293270.html&psig=AOvVaw3lSCwUMqppKQDYSVTMR9Zu&ust=1692667677540000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMDA5M_M7IADFQAAAAAdAAAAABAE",
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




class PostCreateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(name: str,img: str, country: str, born: str, film: str):
        # try:

            data = NormalizeData.process(name = name, img = img, country=country, born = born, film = film)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        name = args_copy["name"]
        img = args_copy["img"]
        country = args_copy["country"]
        born = args_copy["born"]
        film = args_copy["film"]
        response = self.post_process(name = name, img = img, country = country, born= born, film=film)

        return jsonify(response)


api.add_resource(
    PostCreateMovie,
    "/actor/create-actor",
    endpoint="/actor/create-actor",
)
