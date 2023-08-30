from src.models.Mongodb import MongoHelper
from src.common.utils import generateId


class NormalizeData():
    def process(id:str):
        data = MongoHelper.getDocumentInCollectionById(MongoHelper,"movies",id)
        listCast = []

        for i in data["casts"]:
            dictCast = MongoHelper.getDocumentInCollectionById(MongoHelper,"actor",i)
            listCast.append(dictCast)

        if data:
            return {
                "_id": data["_id"],
                "imgBg": data["imgBGr"],
                "name": data["name"],
                "description": data["description"],
                "genres": data["genres"],
                "casts": listCast
            }
        else: 
            return 'Somethings fail went get movie'

