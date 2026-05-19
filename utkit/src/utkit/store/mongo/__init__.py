from pymongo import AsyncMongoClient,MongoClient as SyncMongoClient
import certifi
from typing import Literal


class MongoClient:
    def __new__(cls, uri: str, type: Literal["async", "sync"] = "async") -> AsyncMongoClient | SyncMongoClient:
        instance = super().__new__(cls)

        if type == "async":
            instance.client = AsyncMongoClient(
                uri,
                tls=True,
                tlsCAFile=certifi.where()
            )
        else:
            instance.client = SyncMongoClient(
                uri,
                tls=True,
                tlsCAFile=certifi.where()
            )

        return instance.client
