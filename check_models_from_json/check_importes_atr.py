from common_config import IMPORTES_ATR_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.atr_amount.atr_amount import Atr_Amount

if __name__ == '__main__':

    instance_data = get_entity_from_samples(IMPORTES_ATR_SAMPLE)
    instance = Atr_Amount(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
