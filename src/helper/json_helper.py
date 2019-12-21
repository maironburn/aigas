import json
import os
import urllib3
from common_config import URL_BASE, CALENDARIO_SAMPLE
from importlib import import_module


def get_entity_from_samples(json_sample_file):
    if os.path.exists(json_sample_file):
        with open(json_sample_file) as json_file:
            data = json.load(json_file)
        return data


def check_field_integrity(fields_to_check, json_entity_data):
    module = import_module('common_config')
    for i in getattr(module, fields_to_check):
        if i not in json_entity_data.keys():
            return False
    return True


def get_entity_from_rest(from_date, entity):
    '''

    '''
    http = urllib3.PoolManager()
    params = {
    }
    r = http.request('GET', URL_BASE)

    return json.loads(r.data.decode('utf-8'))
