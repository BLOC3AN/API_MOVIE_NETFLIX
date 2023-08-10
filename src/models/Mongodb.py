from pymongo.mongo_client import MongoClient
class mongoCompass:
    def __init__(self):
        print("Hello MongoDB")

    def connect(self,uri):

        self.uri = uri
        self.client = MongoClient(uri)

        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


    def listDatabase(self):
        # Lấy danh sách tên cơ sở dữ liệu
        self.database_list = self.client.list_database_names()
        print("Databases:",self.database_list)
        return self.database_list
    
    def listCollection(self, database):
        self.col = self.client[database]
        self.listCollections = self.col.list_collection_names()
        print("Current Database:",database,"\nCollections:",self.listCollections)
        return self.listCollections
    
    def insertDocument(self, col, info):
        return self.col[col].insert_one(info)
        
    

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
mongo.insertDocument("info",data)

