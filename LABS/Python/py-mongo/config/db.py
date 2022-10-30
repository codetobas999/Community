from pymongo import MongoClient
#conn = MongoClient("mongodb://root:123456@localhost:27017")
dbName = 'example'
db = MongoClient(
    host = 'localhost:27017', # <-- IP and port go here
    serverSelectionTimeoutMS = 3000, # 3 second timeout
    username="root",
    password="123456" 
)
db = db['' + dbName +'']


