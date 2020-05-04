from pymongo import MongoClient
import logging

class Mongo:
    def __init__(self):
        self.client = MongoClient(host="192.168.99.100",
                    port=27017, 
                    username="root", 
                    password="123456",
                    authSource="admin")
        self.db = self.client['dadoswhats']
        self.collection = self.db['dadoswhats']
    
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