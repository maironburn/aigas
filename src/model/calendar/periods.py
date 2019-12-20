from logger.app_logger import AppLogger
from common_config import PERIODS_FIELDS
from src.helper.json_helper import check_field_integrity
import json


class Periods(object):
    idPeriod = None  # String
    From = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    To = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    calendarDates = []  # Array<Date (ISO8601 (yyyy-MM-dd))>
    active = []  # Array<Integer>, 1 | 0 (activo/inactivo)

    _logger = None
    entity_data = None

    def __init__(self, **kw):

        self.entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Comprobando la integridad de los campos del Periodo")

        if check_field_integrity(PERIODS_FIELDS, self.entity_data):
            self.idPeriod = self.entity_data['idPeriod']
            self.From = self.entity_data['from']
            self.To = self.entity_data['to']
            self.calendarDates = self.entity_data['calendarDates']
            self.active = self.entity_data['active']

    def get_json(self):

        return {"idPeriod": self.idPeriod,
                "from": self.From,
                "to": self.To,
                "calendarDates": self.calendarDates,
                "active": self.active
                }
