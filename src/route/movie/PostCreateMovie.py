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
    "imgBGr",
    type=str,
    required=True,
    default="https://www.google.com.vn/url?sa=i&url=https%3A%2F%2Faccgroup.vn%2Fbackground-la-gi&psig=AOvVaw0ytTkyBrjnsbicbgVElktw&ust=1692670251610000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMilwprW7IADFQAAAAAdAAAAABAE",
)


parser.add_argument(
    "description",
    type=str,
    required=True,
    default="Best film",
)

parser.add_argument(
    "genres",
    type=str,
    required=True,
    default='Khong xac dinh'
)

parser.add_argument(
    "casts",
    type=str,
    required=True,
    default="Chi Dan"
)


class PostCreateMovie(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

    @staticmethod
    def post_process(name: str, imgBGr:str, description:str, genres:str, casts: str):
        # try:

            data = NormalizeData.process(name=name, imgBGr=imgBGr, description=description, genres=genres, casts=casts)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        args_copy = args.copy()
        name = args_copy["name"]
        imgBGr = args_copy["imgBGr"]
        description = args_copy["description"]
        genres = args_copy["genres"]
        casts = args_copy["casts"]

        response = self.post_process(name=name, imgBGr=imgBGr, description=description, genres=genres, casts=casts)

        return jsonify(response)


api.add_resource(
    PostCreateMovie,
    "/movie/create-movie",
    endpoint="/movie/create-movie",
)
