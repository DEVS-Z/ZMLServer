from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class ConnectionHelper:
    _client = None
    _database = None

    @classmethod
    def init_connection(cls):
        if cls._client is None:
            connectionString = os.getenv("MONGO_URI")
            databaseString = os.getenv("MONGO_DATABASE")
            cls._client = MongoClient(connectionString)
            cls._database = cls._client[databaseString]

    @classmethod
    def insert(cls, collection, data):
        if cls._database is None:
            cls.init_connection()
        cls._database[collection].insert_one(data)
