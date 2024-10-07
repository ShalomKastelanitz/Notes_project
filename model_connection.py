from pymongo import MongoClient
class notesModel:
    def __init__(self,mongo_uri, db_name):
       self.client=MongoClient(mongo_uri)
       self.db=self.client[db_name]
       self.collection=self.db['notes']



