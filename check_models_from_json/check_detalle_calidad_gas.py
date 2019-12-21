from common_config import DETALLE_CALIDAD_GAS_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.detalle_calidad_gas.detalle_calidad_gas import QualityGasDetail

if __name__ == '__main__':

    instance_data = get_entity_from_samples(DETALLE_CALIDAD_GAS_SAMPLE)
    instance = QualityGasDetail(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
