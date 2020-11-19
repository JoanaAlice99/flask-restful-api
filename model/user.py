from config.db import db

#user = { "name": "Joana", "age": 21 }

class UserModel():

    def __init__(self):
        self.collection = db.my_db["user"]

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
    