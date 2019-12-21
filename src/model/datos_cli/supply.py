from logger.app_logger import AppLogger
from common_config import Periods_FIELDS
from src.helper.json_helper import check_field_integrity
import json


class Supply(object):
    CUPS = None  # String
    address = None  # String
    locality = None  # String
    postalCode = []  # String
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
            self.CUPS = self.json_entity_data['CUPS']
            self.address = self.json_entity_data['address']
            self.locality = self.json_entity_data['locality']
            self.postalCode = self.json_entity_data['postalCode']
            self.position = self.json_entity_data['position']
        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"CUPS": self.CUPS,
                "address": self.address,
                "locality": self.locality,
                "postalCode": self.postalCode,
                "position": self.position
                }
