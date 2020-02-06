import json
import os
from importlib import import_module
import urllib3
from common_config import LOCAL_ENDPOINT_URL
import datetime


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


def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_date_from_string(date_as_string):
    return datetime.datetime.strptime(date_as_string, "%Y-%m-%d").date()


def get_entity_from_rest(from_date, entity):
    http = urllib3.PoolManager()
    r = http.request('GET', LOCAL_ENDPOINT_URL)

    return json.loads(r.data.decode('utf-8'))