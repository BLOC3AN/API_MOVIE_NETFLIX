from src.models.Mongodb import MongoHelper


class NormalizeData():
    @staticmethod
    def process(id: str, name: str, country: str, film: str):

        param={
                "id":id,
                "name": name,
                "country": country,
                "film": film 
            } 

        data = MongoHelper.updateDocumentInCollection(MongoHelper,'actor',param)
        if data:
            return data
        else: 
            return 'Somethings fail went create movies'
