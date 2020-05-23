from pymongo import MongoClient
import logging
from  configparser import ConfigParser

config = ConfigParser()
config.read("./mongo.conf")

class Mongo:
    def __init__(self):
        self.client = MongoClient(host=config.get("MONGO","host"),
                    port=int(config.get("MONGO","port")), 
                    username=config.get("MONGO","username"), 
                    password=config.get("MONGO","password"),
                    authSource=config.get("MONGO","authSource"))
        self.db = self.client[config.get("MONGO","db")]
        self.collection = self.db[config.get("MONGO","collection")]
    
    def insert(self, data):
        obj_id = self.collection.insert_one(data).inserted_id
        logging.info('Object saved '+str(obj_id))
        return str(obj_id)

    def getAll(self, query):
        obj = self.collection.find(query)
        logging.info('Object found '+str(obj))
        return obj

    def updateByID(self, id, newValue):
        try:
            obj = self.collection.update_one({"_id":id}, newValue)
            logging.info('Object updated '+str(id))
        except:
            logging.info('Object update fail '+str(id))
        return True