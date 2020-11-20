from config.db import Database
from config.key import keys

db = Database()

class UserModel(object):

    def __init__(self):
        #self.db             = db.my_client[keys["mongo_client"]["database"]]
        self.collection     = db.my_db["user"]

    def find_all(self):
        users = self.collection.find()
        return users

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
        update = self.collection.update_one({ "_id": id }, values)
        return update
    
    def delete_by_id(self, id):
        delete = self.collection.delete_one({ "_id": id })
        return delete
    