from common_config import PRECIO_FORMULA_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.formula_price.formula_price import Formula_Price

if __name__ == '__main__':
    instance_data = get_entity_from_samples(PRECIO_FORMULA_SAMPLE)
    instance = Formula_Price(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
