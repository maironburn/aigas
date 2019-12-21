from common_config import CALENDARIO_B70_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.b70_calendar.b70_calendar import B70_Calendar

if __name__ == '__main__':

    instance_data = get_entity_from_samples(CALENDARIO_B70_SAMPLE)
    instance = B70_Calendar(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
