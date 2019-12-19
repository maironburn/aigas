from logger.app_logger import AppLogger
from common_config import PERIODS_FIELDS
from src.helper.json_helper import check_field_integrity
import json


class Periods(object):

    _idPeriod = None  # String
    _from = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _to = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _calendar_dates = []  # Array<Date (ISO8601 (yyyy-MM-dd))>
    _active = []  # Array<Integer>, 1 | 0 (activo/inactivo)

    _logger = None
    entity_data = None

    def __init__(self, **kw):

        self.entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Comprobando la integridad de los campos del Periodo")

        if check_field_integrity(PERIODS_FIELDS, self.entity_data):
            self.id_period = self.entity_data['idPeriod']
            self.from_date = self.entity_data['from']
            self.to_date = self.entity_data['to']
            self.calendar_dates = self.entity_data['calendarDates']
            self.active = self.entity_data['active']

    def get_json(self):

        return {"idPeriod": self.id_period,
                "from": self.from_date,
                "to": self.to_date,
                "calendarDates": self.calendar_dates,
                "active": self.active
                }

    # <editor-fold desc="getter and setters">

    @property
    def id_period(self):
        return self._idPeriod

    @id_period.setter
    def id_period(self, id_period):
        if id_period:
            self._idPeriod = id_period

    @property
    def from_date(self):
        return self._from

    @from_date.setter
    def from_date(self, from_date):
        if from_date:
            self._from = from_date

    @property
    def to_date(self):
        return self._to

    @to_date.setter
    def to_date(self, to_date):
        if to_date:
            self._to = to_date

    # Array<Date (ISO8601 (yyyy-MM-dd))>
    @property
    def calendar_dates(self):
        return self._calendar_dates

    @calendar_dates.setter
    def calendar_dates(self, calendar_dates):
        if calendar_dates:
            self._calendar_dates = calendar_dates

    # Array<Integer>, 1 | 0 (activo/inactivo)
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        if active:
            self._active = active

    # </editor-fold>
