from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(id: str, genre: list):
        data = MongoHelper.updateDocumentInCollection(MongoHelper, 'genre', {
            "id": id,
            "genre": genre,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'



