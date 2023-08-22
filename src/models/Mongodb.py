from pymongo.mongo_client import MongoClient
from bson.json_util import dumps, loads
import json
# from src.enviroments.config import URI_MONGO_URL
URI_MONGO_URL = "mongodb+srv://lethhai3003:jjbufU4yfKCUQLrT@cluster0.wsot8bn.mongodb.net/"

class MongoHelper:
    def __init__(self):
        self.uri = URI_MONGO_URL
        self.client = MongoClient(self.uri)

    def __to_json(self, data):
        from bson.json_util import dumps, loads

        return loads(dumps(list(data)))

    def connect(self,uri):

        self.uri = uri
        self.client = MongoClient(uri)

        try:
            self.client.admin.command('ping')

        except Exception as e:
            print(e)

    def __to_json(self, data):
     
        return loads(dumps(list(data)))
    
    def getDocumentsInCollection(self, collectionName: str):
        return self.__to_json(self, MongoClient(URI_MONGO_URL)['movies'][collectionName].find({}))
        
    def createDocumentInCollection(self, collectionName: str, param: dict):
        return MongoClient(URI_MONGO_URL)['movies'][collectionName].insert(param)
    
    def deleteDocumentInCollection(self, collectionName: str, id: str):
        delete_result = MongoClient(URI_MONGO_URL)['movies'][collectionName].delete_one({
            "_id": id
        })
        
        deleted_count = delete_result.deleted_count
        serialized_deleted_count = json.dumps(deleted_count)
        return serialized_deleted_count
    
    def updateDocumentInCollection(self, collectionName: str, param: dict):
        filter = {"_id": param["id"]}
        param.pop("id")

        update_operation = {"$set":param}

        # Perform the update operation using update_one()
        result = MongoClient(URI_MONGO_URL)['movies'][collectionName].update_one(filter, update_operation)
        return json.dumps(result.modified_count)
    
    def getDocumentInCollectionById(self, collectionName: str, id: str):
        return self.__to_json(self, MongoClient(URI_MONGO_URL)['movies'][collectionName].find({"_id":id}))[0]

    
    def getDocumentsByProperty(self, collectionName: str, property):
        return MongoClient(URI_MONGO_URL)['movies'][collectionName][property]

