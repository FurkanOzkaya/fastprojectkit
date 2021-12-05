from utils.singleton import Singleton
from database.mongodb_functions import MongoDB
from utils.common_functions import date_to_iso_date, get_password_hash
from bson.objectid import ObjectId
from configs import config


class UserDB(MongoDB, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.collection = self.database[config.COLLECTION_NAME_USER]

    def get_user_with_email(self, email):
        result = self.collection.find_one({"email": email}, {"password": 0})
        return result

    def get_user_with_username(self, username):
        result = self.collection.find_one({"username": username}, {"password": 0})
        return result

    def get_user_with_email_include_password(self, email):
        result = self.collection.find_one({"email": email})
        return result

    def get_user_with_object_id(self, object_id):
        result = self.collection.find_one({"_id": ObjectId(str(object_id))})
        return result

    def get_all_documents(self, date_time=None):
        match = {}
        if date_time:
            date_time = date_to_iso_date(date_time)
            match = {"create_time": {"$gte": date_time}}

        result = self.collection.find(match, {"_id": 0, "password": 0})
        return result

    def is_array_element_exist(self, pipeline_func, *args, **kwargs):
        '''
            check there is element in array or not
            pipeline func is object which include search data
        '''
        search_data = pipeline_func(*args, **kwargs)
        result = self.collection.find(search_data)
        res = list(result)
        if res:
            return True
        else:
            return False

    def insert_one(self, insert_value):
        insert_value['password'] = get_password_hash(insert_value['password'])
        return super().insert_one(insert_value)

    def update_password(self, id, data):
        query = {"_id": ObjectId(str(id))}
        data["password"] = get_password_hash(data['password'])
        new_data = {"$set": data}
        result = self.collection.update_one(query, new_data)

        return result.matched_count > 0

    def delete_array_element(self, object_id, delete_data):
        result = self.collection.update_one({"_id": ObjectId(str(object_id))}, {"$pull": delete_data})
        return result

# datetime.strptime(date, '%y-%m-%d %H:%M:%S')
