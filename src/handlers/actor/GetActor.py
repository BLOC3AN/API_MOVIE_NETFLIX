from src.models.Mongodb import MongoHelper


class NormalizeData():
    def process(id:str):
        data = MongoHelper.getDocumentInCollectionById(MongoHelper,"actor",id)
        print(data, "data")

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'

