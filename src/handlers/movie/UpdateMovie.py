from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(id: str,name: str, genre: str, cast: str):
        data = MongoHelper.updateDocumentInCollection(MongoHelper, 'movies', {
            "id": id,
            "name": name,
            "genre": genre,
            "cast": cast
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'



