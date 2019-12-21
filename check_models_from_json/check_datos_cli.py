from common_config import DATOS_CLI_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.cli.cli import CLI

if __name__ == '__main__':

    instance_data = get_entity_from_samples(DATOS_CLI_SAMPLE)
    instance = CLI(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
