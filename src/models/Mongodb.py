from pymongo.mongo_client import MongoClient
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

    def getDocumentsInCollection(self, collectionName: str):
        return self.__to_json(self, MongoClient(URI_MONGO_URL)['movies'][collectionName].find({}))
        
    def createDocumentInCollection(self, collectionName: str, param: dict):
        return self.col[collectionName].insert_one(param)
    
    def deleteDocumentInCollection(self, collectioName: str, id: str):
        return self.col[collectioName].drop(id)
    
    def updateDocumentInCollection(self, collectionName: str, param: dict, newvalue: dict):
        return self.col[collectionName].update_one(param, newvalue)
    
    def getDocumentInCollectionById(self, collectionName: str, id: str):
        return self.col[collectionName].find({"_id": id})
    
    def getDocumentsByProperty(self, collectionName: str, property):
        return self.col[collectionName][property]

    # def createDatabase(self, name, collName):
    #     newdb = self.client[name]
    #     newdb.create_collection(collName)
    #     return newdb
    
    # def listDatabase(self):
    #     # Lấy danh sách tên cơ sở dữ liệu
    #     self.database_list = self.client.list_database_names()
    #     return self.database_list
    
    # def deleteDatabase(self, nameDb):
    #     return self.client.drop_database(nameDb)
    
    # def insertCollection(self,database, collName):
    #     db = self.client[database]
    #     newColl = db.create_collection(collName)
    #     return newColl
    
    # def listCollection(self, database):
    #     self.col = self.client[database]
    #     self.listCollections = self.col.list_collection_names()
    #     return self.listCollections
    
    # def deleteCollection(self, nameDb,nameColl):
    #     return self.client[nameDb].drop_collection(nameColl)
    
    # def showDocument(self, col):
    #     listDoc = []
    #     for i in self.col[col].find():
    #         listDoc.append(i)
    #     return listDoc

    # def insertDocument(self, col, info):
    #     return self.col[col].insert_one(info)
        
    # def deleteDocument_One(self, col, key):
    #     return self.col[col].delete_one(key)
    
    # def deleteDocument_Many(self, col, key):
    #     return self.col[col].delete_many(key)   
    
