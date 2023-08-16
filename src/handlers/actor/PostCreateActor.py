from src.models.Mongodb import MongoHelper
import time

class NormalizeData():
    def process(name: str, country: str, born: str, film: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'actor', {
            "_id": NormalizeData.generateId(),
            "name": name,
            "country": country,
            "born" : born,
            "film": film,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create genre'

    
    def generateId():
        return str(round(time.time() * 1000))

