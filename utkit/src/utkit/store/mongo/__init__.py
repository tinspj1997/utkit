from pymongo import AsyncMongoClient


class MongoClient:
    def __init__(self, uri: str):
        self.client = AsyncMongoClient(uri)

    async def get_database(self, name: str):
        return self.client[name]