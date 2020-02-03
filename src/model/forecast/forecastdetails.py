import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class ForecastDetails(object):
    forecast_day = []
    forecast = None
    lastModified = None

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        self.forecast_day = self.json_entity_data['day']
        self.forecast = self.json_entity_data['forecast']
        self.lastModified = self.json_entity_data['lastModified']


    def get_json(self):

        return {"day": self.forecast_day,
                "forecast": self.forecast,
                "lastModified": self.lastModified
                }
