from pymongo.mongo_client import MongoClient
class mongoCompass:
    def __init__(self):
        self.uri = "mongodb+srv://lethhai3003:jjbufU4yfKCUQLrT@cluster0.wsot8bn.mongodb.net/"
        self.client = MongoClient(self.uri)

    def connect(self,uri):

        self.uri = uri
        self.client = MongoClient(uri)

        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def createDatabase(self, name, collName):
        newdb = self.client[name]
        newdb.create_collection(collName)
        return newdb
    
    def listDatabase(self):
        # Lấy danh sách tên cơ sở dữ liệu
        self.database_list = self.client.list_database_names()
        print("Databases:",self.database_list)
        return self.database_list
    
    def deleteDatabase(self, nameDb):
        return self.client.drop_database(nameDb)
    
    def insertCollection(self,database, collName):
        db = self.client[database]
        newColl = db.create_collection(collName)
        return newColl
    
    def listCollection(self, database):
        self.col = self.client[database]
        self.listCollections = self.col.list_collection_names()
        print("Current Database:",database,"\nCollections:",self.listCollections)
        return self.listCollections
    
    def deleteCollection(self, nameDb,nameColl):
        return self.client[nameDb].drop_collection(nameColl)
    
    def showDocument(self, col):
        listDoc = []
        print("Collection:",col)
        for i in self.col[col].find():
            listDoc.append(i)
        return listDoc

    def insertDocument(self, col, info):
        return self.col[col].insert_one(info)
        
    def deleteDocument_One(self, col, key):
        print("Deleted One",key.values())
        return self.col[col].delete_one(key)
    
    def deleteDocument_Many(self, col, key):
        print("Deleted Many",key.values())
        return self.col[col].delete_many(key)   
    
    

mongo = mongoCompass()
Connect = mongo.connect("mongodb+srv://lethhai3003:jjbufU4yfKCUQLrT@cluster0.wsot8bn.mongodb.net/")
listDB = mongo.listDatabase()
listCol = mongo.listCollection("TaiDN")
# data =  {
#     "name": "Truong Tan Tai",
#     "sex": "Bisexual",
#     "born": 2000,
#     "company":"Sun Asterik",
#     "country":"Lam Yen, Dai Minh, Dai Loc, Quang Nam"
#   }
# mongo.insertDocument("info",data)

