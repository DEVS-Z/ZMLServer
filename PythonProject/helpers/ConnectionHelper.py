from pymongo import MongoClient
from dotenv import load_dotenv
import os

class ConnectionHelper:
    load_dotenv()
    connectionString = os.getenv("MONGO_URI")
    databaseString = os.getenv("MONGO_DATABASE")
    client = None
    database = None

    def __init__(self):
        self.client = MongoClient(self.connectionString)
        self.database = self.client[self.databaseString]

    def insert(self, collection, data):
        self.database[collection].insert_one(data)
