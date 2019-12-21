from common_config import CONSUMO_NOCTURNO_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.consumo_nocturno.consumo_nocturno import Consumo_Nocturno

if __name__ == '__main__':

    instance_data = get_entity_from_samples(CONSUMO_NOCTURNO_SAMPLE)
    instance = Consumo_Nocturno(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
