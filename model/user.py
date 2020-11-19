from config.db import db
from config.key import keys

class UserModel(object):

    def __init__(self):
        self.db             = db.my_client[keys["mongo_client"]["database"]]
        self.collection     = self.db["user"]

    def find_by_id(self, id):
        user = self.collection.find_one({ "_id": id })
        return user

    def find_by_username(self, username):
        user = self.collection.find_one({ "username": username })
        return user

    def save(self, user):
        save = self.collection.insert_one(user)
        return save

    def update_by_id(self, id, values):
        delete = self.collection.update_one({ "_id": id }, values)
        return delete
    
    def delete_by_id(self, id):
        delete = self.collection.delete_one({ "_id": id })
        return delete
    