from src.models.Mongodb import MongoHelper
from src.common.utils import   generateId
class NormalizeData():
    def process(name: str, img: str, country: str, born: str, film: str):
        data = MongoHelper.createDocumentInCollection(MongoHelper, 'actor', {
            "_id": generateId(),
            "name": name,
            "img": img,
            "country": country,
            "born" : born,
            "film": film,
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create genre'


