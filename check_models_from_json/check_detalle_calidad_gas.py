from common_config import DETALLE_CALIDAD_GAS_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.gas_quality_detail.gas_quality_detail import Gas_Quality_Detail

if __name__ == '__main__':

    instance_data = get_entity_from_samples(DETALLE_CALIDAD_GAS_SAMPLE)
    instance = Gas_Quality_Detail(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".format(instance.unique,
                                                                                                 instance.is_temporal_sequence,
                                                                                                 instance.collection_name,
                                                                                                 instance.collection_name_rev))
    print("Entidad:\n {}".format(instance_json))