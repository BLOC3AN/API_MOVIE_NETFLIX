from pymongo.mongo_client import MongoClient
# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://lethhai3003:U7UJf16dTHjUuBXh@cluster0.oqg68nh.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Lấy danh sách tên cơ sở dữ liệu
database_list = client.list_database_names()

# In danh sách các cơ sở dữ liệu
for db_name in database_list:
    print(db_name)


# Chon database myFirstDatabase
myFirstDatabase = client["user"]
listCollectionNames = myFirstDatabase.list_collection_names()

# myFirstDatabase["VIP"].insert_one(
#  {
#     "title": "The Favourite",
#     "genres": [ "Drama", "History" ],
#     "runtime": 121,
#     "rated": "R",
#     "year": 2018,
#     "directors": [ "Yorgos Lanthimos" ],
#     "cast": [ "Olivia Colman", "Emma Stone", "Rachel Weisz" ],
#     "type": "movie"
#   }
# )
#find Documents     
findDocument = myFirstDatabase.VIP.find_one()
print(findDocument["_id"])
