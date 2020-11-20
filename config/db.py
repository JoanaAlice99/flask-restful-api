from pymongo import MongoClient
from config.key import keys

class Database():

    def __init__(self):
        self.host   = str(keys["mongo_client"]["host"])
        self.port   = int(keys["mongo_client"]["port"])
        self.my_client = MongoClient(self.host,self.port)
        self.my_db  = self.my_client[keys["mongo_client"]["database"]]
        self.my_collection = {}


    def connect(self):
        try:
            self.my_client = MongoClient(self.host,self.port)
            self.my_db = self.my_client[keys["mongo_client"]["database"]]
        except:
            print("Connection to the database failed")

    def disconnect(self):
        try:
            self.my_client.close()
            print("Connection to the database closed")
        except:
            print("Failed to close connection with the database")