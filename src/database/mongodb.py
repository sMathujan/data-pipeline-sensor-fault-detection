import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        #Make connection with MongoDB
        MONGO_DB_URL = ""
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        # self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        self.db_name="ineuron"

    # Insert many records into MongoDB
    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    # Insert one record at a time
    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)

    # In this project, we dump the 5000 records into MongoDB at a time.
    # If we dump the record one by one, it will complicate the MongoDB
        
