from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(id: str):
        data = MongoHelper.deleteDocumentInCollection(MongoHelper, 'movies', id)
        print(data)

        if data:
            return data
        else: 
            return 'Somethings fail went delete movies'


