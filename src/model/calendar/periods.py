import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Periods(object):
    id_period = str
    _from = str
    _to = str
    calendar_dates = []
    dates = []
    active = []
    last_modified = str

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):
        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        self.id_period = self.json_entity_data['idPeriod']
        self._from = self.json_entity_data['from']
        self._to = self.json_entity_data['to']
        self.last_modified = self.json_entity_data['lastModified']
        self.calendar_dates = self.json_entity_data['calendarDates']
        self.active = self.json_entity_data['active']
        self.dates = self.json_entity_data['dates']

    def get_json(self):
        return {"idPeriod": self.id_period,
                "from": self._from,
                "to": self._to,
                "lastModified": self.last_modified,
                "calendarDates": self.calendar_dates,
                "active": self.active,
                "dates": self.dates
                }
