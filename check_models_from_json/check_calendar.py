from common_config import CALENDARIO_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.calendar.calendar import Calendar

if __name__ == '__main__':
    instance_data = get_entity_from_samples(CALENDARIO_SAMPLE)
    instance = Calendar(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".format(instance.unique,
                                                                                                 instance.is_temporal_sequence,
                                                                                                 instance.collection_name,
                                                                                                 instance.collection_name_rev))
    print("Entidad:\n {}".format(instance_json))

    # print("conexion a la base de datos")
    # db = connect_to()
    # print("conectado")
    # inserted_id = db.calendario.insert_one(calendario_json).inserted_id
    # print("{}".format(inserted_id))