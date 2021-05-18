from database.mongodb_functions import MongoDB
from utils.singleton import Singleton
from utils.common_functions import date_to_iso_date, get_password_hash


class UserDB(MongoDB, metaclass=Singleton):
    def __init__(self, host='localhost', port=27017, username='', password='', database=None, collection=None):
        super().__init__(host=host, port=port, username=username, password=password, database=database, collection=collection)

    def get_user_with_email(self, email):
        result = self.collection.find_one({"email": email}, {"_id": 0, "password": 0})
        return result

    def get_user_with_email_pass(self, email):
        result = self.collection.find_one({"email": email}, {"_id": 0})
        return result

    def insert_one(self, insert_value):
        insert_value['password'] = get_password_hash(insert_value['password'])
        return super().insert_one(insert_value)

    def update_one(self, email, data):
        query = {"email": email}
        new_data = {"$set": data}
        result = self.collection.update_one(query, new_data)

        return result.matched_count > 0

    def update_password(self, email, data):
        query = {"email": email}
        print(data)
        data["password"] = get_password_hash(data['password'])
        new_data = {"$set": data}
        result = self.collection.update_one(query, new_data)

        return result.matched_count > 0

    def get_all_documents(self, date_time=None):
        match = {}
        if date_time:
            date_time = date_to_iso_date(date_time)
            match = {"create_time": {"$gte": date_time}}

        result = self.collection.find(match, {"_id": 0, "password": 0})
        return result
#datetime.strptime(date, '%y-%m-%d %H:%M:%S')
