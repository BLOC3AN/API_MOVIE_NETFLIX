from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(name: str, genre: str, cast: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'movies', {
            "_id": NormalizeData.generateId(),
            "name": name,
            "genre": genre,
            "cast": cast
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'

    
    def generateId():
        return str(round(time.time() * 1000))

