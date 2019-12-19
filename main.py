import json
from src.helper.json_helper import get_entity_from_samples
from common_config import CALENDARIO_SAMPLE
from src.model.calendario.calendario import Calendario
import pymongo
from pymongo import MongoClient

def get_db():
    host = "localhost"
    puerto = "27017"
    '''
    usuario = "usuario"
    pwd = "pwd"   
    '''
    bbdd = "airegas"
    #cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
    cliente = MongoClient("mongodb://{}:{}".format( host, puerto))

    return cliente[bbdd]


if __name__ == '__main__':
    calendario_data = get_entity_from_samples(CALENDARIO_SAMPLE)
    cal = Calendario(**{'entity_data': calendario_data})
    calendario_json= cal.get_json()
    print ("Entidad:\n {}" .format(calendario_json))

    print("conexion a la base de datos")
    conection = get_db()
    print("conectado")
    inserted_id = conection.calendario.insert_one(calendario_json).inserted_id
    print("{}".format(inserted_id))