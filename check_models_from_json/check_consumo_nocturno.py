from common_config import CONSUMO_NOCTURNO_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.night_consumption.night_consumption import Night_Consumption

if __name__ == '__main__':

    instance_data = get_entity_from_samples(CONSUMO_NOCTURNO_SAMPLE)
    instance = Night_Consumption(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".format(instance.unique,
                                                                                                 instance.is_temporal_sequence,
                                                                                                 instance.collection_name,
                                                                                                 instance.collection_name_rev))
    print("Entidad:\n {}".format(instance_json))
