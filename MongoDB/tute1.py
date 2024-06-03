import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db=client['Saurabh']