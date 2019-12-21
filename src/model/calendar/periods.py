import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Periods(object):
    idPeriod = None  # String
    From = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    To = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    calendarDates = []  # Array<Date (ISO8601 (yyyy-MM-dd))>
    active = []  # Array<Integer>, 1 | 0 (activo/inactivo)

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self.idPeriod = self.json_entity_data['idPeriod']
            self.From = self.json_entity_data['from']
            self.To = self.json_entity_data['to']
            self.calendarDates = self.json_entity_data['calendarDates']
            self.active = self.json_entity_data['active']
        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"idPeriod": self.idPeriod,
                "from": self.From,
                "to": self.To,
                "calendarDates": self.calendarDates,
                "active": self.active
                }
