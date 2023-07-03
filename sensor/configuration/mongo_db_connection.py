import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
from sensor.logger import logging
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                # logging.info(f"db Connection url:{os.environ["MONGODB_URL_KEY"]}")
                mongo_db_url = "mongodb+srv://sudeshb94:sudesh94@cluster0.nyotrwr.mongodb.net/?retryWrites=true&w=majority"
                # MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name

        except Exception as e:
            raise e


