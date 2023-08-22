from src.models.Mongodb import MongoHelper
from src.common.utils import   generateId
class NormalizeData():
    def process(name: str, img: str, country: str, yearOfBirth: str, films: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'actor', {
            "_id": generateId(),
            "name": name,
            "img": img,
            "country": country,
            "yearOfBirth" : yearOfBirth,
            "films": films,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create genre'


