from src.models.Mongodb import MongoHelper
from src.common.utils import generateId

class NormalizeData():
    def process(name: str, genre: str, cast: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'movies', {
            "_id": generateId(),
            "name": name,
            "genre": genre,
            "cast": cast
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'

    


