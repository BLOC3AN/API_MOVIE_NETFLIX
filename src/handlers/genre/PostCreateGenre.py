from src.models.Mongodb import MongoHelper
from src.common.utils import  generateId

class NormalizeData():
    def process(genres: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'genre', {
            "_id": generateId(),
            "genres": genres,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create genre'


