from src.models.Mongodb import MongoHelper
from src.common.utils import generateId

class NormalizeData():
    def process(name: str,imgBGr:str, description:str, genres: str, casts: str):

        data = MongoHelper.createDocumentInCollection(MongoHelper, 'movies', {
            "_id": generateId(),
            "imgBGr" : imgBGr,
            "name": name,
            "description": description,
            "genres": genres.split(","),
            "casts": casts.split(",")
        })

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'

    


