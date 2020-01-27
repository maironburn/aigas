import json
from datetime import datetime
from common_config import collection_mapper
from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class AireGas(object):
    _id = None  # String
    ts = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    _logger = None
    json_entity_data = None
    is_temporal_sequence = None
    _last_modified = datetime
    _collection_name = None  # coleccion para instancias de nueva creacion | actualizadas
    _collection_name_old = None  # coleccion para historico

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        #self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        if isinstance(self.json_entity_data, dict):
            print("Loading data {} from json".format(self.__class__.__name__))
            self.collection_name ="{}".format(collection_mapper[self.__class__.__name__]).lower()
            self.collection_name_old = "{}_old".format(collection_mapper[self.__class__.__name__]).lower()
            self.load_data()

    def load_data(self):
        print("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))
        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self._id = self.json_entity_data['_id']
            self.ts = self.json_entity_data['ts'] if 'ts' in self.json_entity_data.keys() else 'None'
            #self._last_modified =datetime.now().replace(microsecond=0).isoformat()
            self._last_modified = self.json_entity_data['last_modified'] if 'last_modified' in self.json_entity_data.keys() else '2020-01-01'
        else:
            print("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    # <editor-fold desc="getter and setters">
    def get_json(self):
        return {#"_id": self._id,
                #"ts": self.ts,
                "last_modified": self._last_modified
                }

    def get_db_last_update(self):
        print("todo")

    @property
    def unique(self):
        # identificador univoco de la entidad
        raise NotImplementedError

    @property
    def collection_name(self):
        # identificador univoco de la entidad
        return self._collection_name

    @collection_name.setter
    def collection_name(self, value):
        if value:
            self._collection_name = value

    @property
    def collection_name_old(self):
        # identificador univoco de la entidad
        return self._collection_name_old

    @collection_name_old.setter
    def collection_name_old(self, value):
        if value:
            self._collection_name_old = value