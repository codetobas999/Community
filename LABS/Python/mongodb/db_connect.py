from pymongo import MongoClient
from datetime import timedelta
import datetime 
#client = MongoClient("mongodb://{user}:{password}@{host}:{port}")
#db = client.{database}
client = MongoClient("mongodb://root:123456@localhost:27017")
db = client.example
try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
#-----------------
tb = db['BBBB']
tb.insert_one({ "name": "Etherium99", "symbol": "ETH99" ,"last_modified": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
tb.insert_many([
               { "name": "bas", "symbol": "bas11" ,"last_modified": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') },
               { "name": "bas9", "symbol": "bas22","last_modified": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') }
              ]) 
#-----------------
result = tb.find_one({"name":"Etherium99"})
print("--------------------*1")
print(result)
print("--------------------")
print(datetime.datetime.now() - timedelta(minutes=1))
result = tb.find({ "last_modified":{"$gt": datetime.datetime.now() - timedelta(minutes=1)  , "$lt":datetime.datetime.now() } })
print("--------------------*2")
print(result)
print("--------------------")
  
result = tb.find()
for mydata in result:
    print(mydata)
#-----------------
tb.update_one({"name":"Etherium99"},
              {"$set":{"name":"Etherium88","symbol": "ETH88"}}
             )

tb.update_many({"name":"bas"},
               {"$set":{"name":"bas9","symbol": "bas9"}}
              )
#-----------------
tb.delete_one({"name":"Etherium99"})
print("Deleted")

tb.delete_many({"name":"bas9"})
print("Deletes")

#tb.delete_many({})
#print("Deleted All")

client.close()