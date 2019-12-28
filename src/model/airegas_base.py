import json
from datetime import datetime

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class AireGas(object):
    _id = None  # String
    ts = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _logger = None
    json_entity_data = None
    is_temporal_sequence = None

    collection_name = None  # coleccion para instancias de nueva creacion | actualizadas
    collection_name_rev = None  # coleccion para historico

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        if isinstance(self.json_entity_data, dict):
            self._logger.info("Loading data {} from json".format(self.__class__.__name__))
            self.collection_name = "{}".format(self.__class__.__name__.lower())
            self.collection_name_rev = "{}_old".format(self.__class__.__name__.lower())
            self.load_data()

    def load_data(self):
        self._logger.info("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))
        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self._id = self.json_entity_data['_id']
            # self.ts = self.entity_data['ts'] = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
            self.ts = datetime.now().replace(microsecond=0).isoformat()
        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    # <editor-fold desc="getter and setters">
    def get_json(self):
        return {"_id": self._id,
                "ts": self.ts
                }

    def get_db_last_update(self):
        pass

    @property
    def unique(self):
        # identificador univoco de la entidad
        raise NotImplementedError

