import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class NominationDetails(object):
    day = None
    expiration_date = None
    last_modified = None
    nomination = None
    _logger = None
    json_entity_data = None

    def __init__(self, **kw):
        self.json_entity_data = kw.get('entity_data', None)
        self.load_data()

    def load_data(self):
        self.day = self.json_entity_data['day']
        self.expiration_date = self.json_entity_data['expirationDate']
        self.last_modified = self.json_entity_data['lastModified']
        self.nomination = self.json_entity_data['nomination']

    def get_json(self):
        return {"day": self.day,
                "expirationDate": self.expiration_date,
                "lastModified": self.last_modified,
                "nomination": self.nomination
                }
