import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Supply(object):
    cups = None  # String
    address = None  # String
    locality = None  # String
    postal_code = []  # String
    position = []  # String

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self.cups = self.json_entity_data['CUPS']
            self.address = self.json_entity_data['address']
            self.locality = self.json_entity_data['locality']
            self.postal_code = self.json_entity_data['postalCode']
            self.position = self.json_entity_data['position']
        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"CUPS": self.cups,
                "address": self.address,
                "locality": self.locality,
                "postalCode": self.postal_code,
                "position": self.position
                }
