import json
from src.helper.json_helper import get_entity_from_samples
from common_config import CONSUMO_SAMPLE
from src.model.consumo.consumo import Consumo
from src.mongodb.mongo_client import connect_to

if __name__ == '__main__':

    instance_data = get_entity_from_samples(CONSUMO_SAMPLE)
    instance = Consumo(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
