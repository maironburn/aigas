import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Nomination_Details(object):
    day = str
    expirationDate = str
    lastModified = str
    nomination = None
    _logger = None
    json_entity_data = None

    def __init__(self, **kw):
        self.json_entity_data = kw.get('entity_data', None)
        # self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        # self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        self.day = self.json_entity_data['day']
        self.expirationDate = self.json_entity_data['expirationDate']
        self.lastModified = self.json_entity_data['lastModified']
        self.nomination = self.json_entity_data['nomination']

    def get_json(self):
        return {"day": self.day,
                "expirationDate": self.expirationDate,
                "lastModified": self.lastModified,
                "nomination": self.nomination
                }
