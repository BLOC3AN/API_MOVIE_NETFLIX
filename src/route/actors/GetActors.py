from flask import jsonify
from app import api
from src.common.ResponseSuccess import response as ResponseSuccess
from src.common.ResponseError import response as ResponseError
from src.handlers.actors.GetActors import NormalizeData
from flask_restx import Resource, reqparse

parser = reqparse.RequestParser()


class GetMovies(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs) 

    @staticmethod
    def get_process():
        # try:
            listGennes = NormalizeData.process()
            return ResponseSuccess(listGennes)
        # except:
        #     return ResponseError()
        
    @api.doc(parser=parser)
    def get(self):
        data = self.get_process()
        return jsonify(data)

api.add_resource(GetMovies, "/movies/get-actors", endpoint="/movies/get-actors")
