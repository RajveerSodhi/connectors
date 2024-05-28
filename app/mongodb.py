from pymongo import MongoClient
from pydantic import BaseSettings

class MongoDBSettings(BaseSettings):
    mongo_uri: str
    mongo_db: str

class MongoDBConnection:
    def __init__(self):
        self.settings = MongoDBSettings()
        self.client = MongoClient(self.settings.mongo_uri)
        self.db = self.client[self.settings.mongo_db]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def close(self):
        self.client.close()