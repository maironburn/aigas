import json
from src.helper.json_helper import get_entity_from_samples
from common_config import CALENDARIO_SAMPLE
from src.model.calendario.calendario import Calendario
from src.mongo.mongo_client import connect_to

if __name__ == '__main__':
    calendario_data = get_entity_from_samples(CALENDARIO_SAMPLE)
    cal = Calendario(**{'entity_data': calendario_data})
    calendario_json = cal.get_json()
    print("Entidad:\n {}".format(calendario_json))

    print("conexion a la base de datos")
    db = connect_to()
    print("conectado")
    inserted_id = db.calendario.insert_one(calendario_json).inserted_id
    print("{}".format(inserted_id))
