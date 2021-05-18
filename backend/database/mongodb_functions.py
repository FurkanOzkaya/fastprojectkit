from re import match
from utils.exceptions import DatabaseError
from pymongo import MongoClient
from utils.singleton import Singleton


class MongoDB(metaclass=Singleton):
    def __init__(self, host='localhost', port=27017, username='', password='', database=None, collection=None):
        try:
            self.client = MongoClient(host=host, port=port, username=username, password=password)
        except:
            raise DatabaseError("Database client creation has been failed!")

        if database is not None and collection is not None:
            self.db = self.client[database]
            self.collection = self.db[collection]

    def insert_one(self, insert_value):
        result = self.collection.insert_one(insert_value)
        return result

    def get_all_documents(self):
        result = self.collection.find({}, {"_id": 0})
        return result

    def aggregate(self, pipeline):
        result = self.collection.aggregate(pipeline)
        return result
