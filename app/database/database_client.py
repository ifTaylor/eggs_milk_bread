from pymongo import MongoClient


class DatabaseClient:
    def __init__(self):
        self.client = None

    def connect(self):
        if not self.client:
            self.client = MongoClient('localhost', 27017)
        return self.client

    def close(self):
        if self.client:
            self.client.close()
