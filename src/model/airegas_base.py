from datetime import datetime
from common_config import collection_mapper


class AireGas(object):
    '''
    Clase base de todas las colecciones de la ingesta de Datos (airegas)
    '''

    _id = None
    ts = None
    _logger = None
    json_entity_data = None
    is_temporal_sequence = None
    _max_last_modified = datetime
    # coleccion para instancias de nueva creacion | actualizadas
    _collection_name = None
    # coleccion para historico
    _collection_name_old = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self.collection_name = "{}".format(collection_mapper[self.__class__.__name__]).lower()
        self.collection_name_old = "{}_old".format(collection_mapper[self.__class__.__name__]).lower()

        if isinstance(self.json_entity_data, dict):
            print("Loading data {} from json".format(self.__class__.__name__))

            self.load_data()

    def load_data(self):
        print("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))

        self._id = self.json_entity_data['_id']
        self.ts = self.json_entity_data['ts'] if 'ts' in self.json_entity_data.keys() else 'None'
        self._max_last_modified = self.json_entity_data['maxLastModified'] \
            if 'maxLastModified' in self.json_entity_data.keys() else ''

    # <editor-fold desc="getter and setters">
    def get_json(self):
        return {
            "ts": self.ts,
            "maxLastModified": self._max_last_modified
        }

    @property
    def unique(self):
        # identificador univoco de la entidad
        raise NotImplementedError

    @property
    def unique_str(self):
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
