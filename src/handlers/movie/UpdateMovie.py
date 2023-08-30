from src.models.Mongodb import MongoHelper

class NormalizeData():
    def process(id: str,name: str,imgBGr:str, description:str, genres: str, cast: str):
        data = MongoHelper.updateDocumentInCollection(MongoHelper, 'movies', {
            "id": id,
            "name": name,
            "imgBGr":imgBGr,
            "description":description,
            "genres": genres,
            "cast": cast
        })

        if data:
            return data
        else: 
            return 'Somethings fail went update movie'



