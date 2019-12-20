from logger.app_logger import AppLogger
from src.model.calendar.periods import Periods
from common_config import Calendar_FIELDS, PERIODS_FIELDS
from src.helper.json_helper import check_field_integrity
from datetime import datetime


class AireGas(object):
    _id = None  # String
    ts = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _logger = None
    entity_data = None
    is_temporal_sequence = True

    def __init__(self, **kw):

        self.entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        if isinstance(self.entity_data, dict):
            self._logger.info("Loading data {} from json".format(self.__class__.__name__))
            self.load_data()

    def load_data(self):
        self._logger.info("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))
        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.entity_data):
            self.id = self.entity_data['_id']
            # self.ts = self.entity_data['ts'] = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
            self.ts = datetime.now().replace(microsecond=0).isoformat()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        return {"_id": self.id,
                "ts": self.ts
                }

    @property
    def unique(self):
        # identificador univoco de la entidad
        raise NotImplementedError

    @property
    def is_temporal_sequence(self):
        # flag que identifica el proceso de revision que se debe realizar
        raise NotImplementedError
