from common_config import CALENDARIO_B70_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.calendar_b70.calendar_b70 import CalendarB70

if __name__ == '__main__':

    instance_data = get_entity_from_samples(CALENDARIO_B70_SAMPLE)
    instance = CalendarB70(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}".format( instance.unique, instance.is_temporal_sequence))
    print("Entidad:\n {}".format(instance_json))
