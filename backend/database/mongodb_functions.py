from bson.objectid import ObjectId
from configs.config import MONGO_HOST, MONGO_PORT, MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD, DATABASE_NAME
from utils.exceptions import DatabaseError
from pymongo import MongoClient
from utils.singleton import Singleton


class MongoDB(metaclass=Singleton):
    def __init__(self):
        self.host = MONGO_HOST
        self.port = MONGO_PORT
        self.mongo_username = MONGO_INITDB_ROOT_USERNAME
        self.mongo_password = MONGO_INITDB_ROOT_PASSWORD
        self.database_name = DATABASE_NAME
        self.connect_mongo()

    def connect_mongo(self):
        try:
            self.client = MongoClient(host=f"{self.host}", port=int(self.port),
                                      username=self.mongo_username, password=self.mongo_password)
        except Exception as err:
            raise DatabaseError("Database client creation has been failed! ", err)

        self.database = self.client[self.database_name]

    def connect_collection(self, collection=None):
        self.collection = collection

        if self.collection is not None:
            self.collection = self.database[self.collection]

    def insert_one(self, insert_value):
        result = self.collection.insert_one(insert_value)
        return result

    def find_one(self, search_value):
        result = self.collection.find_one(search_value)
        return result

    def find(self, search_value, extra_opts=None):
        if extra_opts:
            result = self.collection.find(search_value, extra_opts)
        else:
            result = self.collection.find(search_value)
        return result

    def get_all_documents(self):
        result = self.collection.find({}, {"_id": 0})
        return result

    def aggregate(self, pipeline):
        result = self.collection.aggregate(pipeline)
        return result

    def update_one(self, id, data, set_active=True):
        query = {"_id": ObjectId(id)}
        new_data = {"$set": data}
        if set_active:
            result = self.collection.update_one(query, new_data)
        else:
            result = self.collection.update_one(query, data)
        return result.matched_count > 0

    def update_one_query(self, query, data):
        new_data = {"$set": data}
        result = self.collection.update_one(query, new_data)
        return result

    def add_item_to_array(self, id, data):
        query = {"_id": ObjectId(id)}
        new_data = {"$push": data}
        result = self.collection.update_one(query, new_data)
        return result.matched_count > 0
