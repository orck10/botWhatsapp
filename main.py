import logging
from whats.whatsMensagens import *
from mongo.conection import *
import time
#from  configparser import ConfigParser

'''
config = ConfigParser()
config["MONGO"] = { "host":"$host$",
                    "port":"$port$",
                    "username":"$username$",
                    "password":"$password$",
                    "authSource":"$authSource$",
                    "db":"$db$",
                    "collection":"$collection$"}
with open('./mongo.conf', 'w') as configfile:
    config.write(configfile)
'''

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='info.log', level=logging.INFO)

whats = Whats()
rodar = True
whats.open()
while rodar:
    conexao = Mongo()
    mensgens =  conexao.getAll({"enviado":0})
    for m in mensgens:
        try:
            print(m)
            if m['nomes']:
                enviado = whats.send(m['mensagem'],m['nomes'])
            if m['numeros']:
                enviado = whats.send(m['mensagem'],m['numeros'])
            if enviado == True:
                conexao.updateByID(m['_id'], {"$set":{"enviado":1}})
            else:
                conexao.updateByID(m['_id'], {"$set":{"enviado":0}})
        except:
            conexao.updateByID(m['_id'], {"$set":{"enviado":0}})
    time.sleep(30)
whats.close()
exit()