import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['Anime']

collection = db['movies']


for x in collection.find({},{'title': 'The Movie'}):
    print(x).title