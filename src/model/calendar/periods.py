import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Periods(object):
    idPeriod = str  # String
    From = str  # Date (yyyy-MM-dd)
    To = str  # Date (yyyy-MM-dd)
    calendarDates = []  # Array<Date (ISO8601 (yyyy-MM-dd))>
    dates = []  # CalendarioListPeriodsDates
    active = []  # Array<Integer>, 1 | 0 (activo/inactivo)
    lastModified = str

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):
        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):

        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        self.idPeriod = self.json_entity_data['idPeriod']
        self.From = self.json_entity_data['from']
        self.To = self.json_entity_data['to']
        self.calendarDates = self.json_entity_data['calendarDates']
        self.dates = self.json_entity_data['dates']
        self.lastModified = self.json_entity_data['lastModified']
        self.active = self.json_entity_data['active']

    def get_json(self):
        return {"idPeriod": self.idPeriod,
                "from": self.From,
                "to": self.To,
                "calendarDates": self.calendarDates,
                "dates" : self.dates,
                "lastModified" : self.lastModified,
                "active": self.active
                }
