from src.models.Mongodb import MongoHelper
from src.common.utils import generateId

class NormalizeData():
    def process(id:str):
        data = MongoHelper.getDocumentInCollectionById(MongoHelper,"movies",id)
        print(data, "data")

        if data:
            return data
        else: 
            return 'Somethings fail went create movies'

