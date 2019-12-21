from common_config import TASA_MOLECULA_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.molecule_tax.molecule_tax import Molecule_Tax

if __name__ == '__main__':

    instance_data = get_entity_from_samples(TASA_MOLECULA_SAMPLE)
    instance = Molecule_Tax(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
