from src.mongodb.mongo_client import MongoAireGas
from src.model.airegas_base import AireGas


class MongoController(MongoAireGas):

    _instance = AireGas

    def __init__(self, **kw):
        super().__init__(**kw)
        if kw.get('instance'):
            self.instance = kw.get('instance')

    def set_collection_info(self, instance):

        collection = instance.collection_name
        version_collection = "{}_old".format(collection)
        unique = self.instance.unique

        return {'collection': collection, 'version_collection': version_collection,
                'unique': unique, 'unique_str': instance.unique_str}

    def insert_or_version(self):
        data_db = self.set_collection_info

    @property
    def instance(self):
        # identificador univoco de la entidad
        return self._instance

    @instance.setter
    def instance(self, value):
        if issubclass(value, AireGas):
            self._instance = value
