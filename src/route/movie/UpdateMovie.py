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
    "imgBGr",
    type=str,
    required=True,
    default="https://www.google.com.vn/url?sa=i&url=https%3A%2F%2Faccgroup.vn%2Fbackground-la-gi&psig=AOvVaw0ytTkyBrjnsbicbgVElktw&ust=1692670251610000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMilwprW7IADFQAAAAAdAAAAABAE",
)

parser.add_argument(
    "description",
    type=str,
    required=True,
    default="Bo phim dang xem vao he 2023 nay",
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
    def put_process(id: str,name: str, imgBGr:str, description:str, genre:str, cast: str):
        # try:

            data = NormalizeData.process(id=id, name=name, imgBGr=imgBGr, description=description, genre=genre, cast=cast)

            return ResponseSuccess(data)
    

        # except:
        #     return ResponseError()

    @api.doc(parser=parser)
    def put(self):
        args = parser.parse_args()
        args_copy = args.copy()
        id= args_copy["id"]
        name = args_copy["name"]
        imgBGr = args_copy["imgBGr"]
        description = args_copy["description"]
        genre = args_copy["genre"]
        cast = args_copy["cast"]

        response = self.put_process(id=id,name=name, imgBGr=imgBGr, description=description, genre=genre, cast=cast)

        return jsonify(response)


api.add_resource(
    UpdateMovie,
    "/movie/update-movie",
    endpoint="/movie/update-movie",
)
