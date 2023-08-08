from flask import jsonify
from flask_restx import Resource
from app import api
from src.common.ResponseSuccess import response as ResponseSuccess
from src.common.ResponseError import response as ResponseError

class GetMovies(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs) 

    @staticmethod
    def get_process():
        try:
            return ResponseSuccess('demo')
        except:
            return ResponseError()
    
    def get(self):
        data = self.get_process()

        return jsonify(data)

api.add_resource(GetMovies, "/movies/get-all-movies", endpoint="/movies/get-all-movies")