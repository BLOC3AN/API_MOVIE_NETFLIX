from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(genre: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'genre', {
            "_id": NormalizeData.generateId(),
            "genre": genre,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create genre'

    
    def generateId():
        return str(round(time.time() * 1000))

