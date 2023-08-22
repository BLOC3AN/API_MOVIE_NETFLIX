from src.models.Mongodb import MongoHelper


class NormalizeData():
    def process(id: str):
        data = MongoHelper.deleteDocumentInCollection(MongoHelper, 'actor', id)
        print(data)

        if data:
            return data
        else: 
            return 'Somethings fail went delete movies'


