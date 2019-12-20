from logger.app_logger import AppLogger
from src.model.calendario.periods import Periods
from common_config import CALENDARIO_FIELDS, PERIODS_FIELDS
from src.helper.json_helper import check_field_integrity
from datetime import datetime


class PrecioFormula(object):
    _id = None  # String
    _ts = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _formulaCode = None  # String
    _formulaDes = None  # String

    _from = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _to = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _compoundIndex = None

    _logger = None
    entity_data = None

    def __init__(self, **kw):

        self.entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        if isinstance(self.entity_data, dict):
            self._logger.info("Loading data {} from json".format(self.__class__.__name__))
            self.load_data()

    def load_data(self):
        self._logger.info("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))
        if check_field_integrity(CALENDARIO_FIELDS, self.entity_data):
            self.id = self.entity_data['_id']
            # self.ts = self.entity_data['ts'] = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
            self.ts = datetime.now().replace(microsecond=0).isoformat()
            self.calendar_code = self.entity_data['calendarCode']
            periods = self.entity_data['Periods']

            periods and self.load_periods(periods)

    def load_periods(self, periods):
        self._logger.info("Iniciando la carga de {} periodos asociados al calendario ".format(len(periods)))
        for p in periods:
            if check_field_integrity(PERIODS_FIELDS, p):
                self.periods.append(Periods(**{'entity_data': p, 'logger': self._logger}))

        self._logger.info("Instanciados {} periodos  ".format(len(self.periods)))

    def get_periods(self):

        periods = []
        for p in self.periods:
            periods.append(p.get_json())

        return periods

    # <editor-fold desc="getter and setters">
    def get_json(self):

        return {"_id": self.id,
                "ts": self.ts,
                "calendarCode": self.calendar_code,
                "Periods": self.get_periods()
                }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, identifier):
        if id:
            self._id = identifier

    @property
    def ts(self):
        return self._ts

    @ts.setter
    def ts(self, ts):
        if ts:
            self._ts = ts

    @property
    def calendar_code(self):
        return self._calendar_code

    @calendar_code.setter
    def calendar_code(self, calendar_code):
        if calendar_code:
            self._calendar_code = calendar_code

    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, periods):
        if isinstance(periods, list):
            self._periods = periods

    # </editor-fold>
