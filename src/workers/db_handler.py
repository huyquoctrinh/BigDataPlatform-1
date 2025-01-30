from pymongo import MongoClient

class AtlasClient ():

    def __init__ (
        self, 
        altas_uri, 
        dbname
    ):
       self.mongodb_client = MongoClient(altas_uri)
       self.database = self.mongodb_client[dbname]

    def ping (self):
       self.mongodb_client.admin.command('ping')

    def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection

    def insert(self, collection_name, data):
        collection = self.database["audio_metadata"]
        collection.insert_one(data)
        return True

    def find (self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = list(collection.find(filter=filter, limit=limit))
       return items