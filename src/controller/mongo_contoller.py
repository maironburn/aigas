from src.mongodb.mongo_client import MongoAireGas
from src.model.airegas_base import AireGas
from datetime import datetime
from bson.objectid import ObjectId



class MongoVersionController(MongoAireGas):

    _instance = AireGas
    '''
    Clase para satisfacer las necesidades del versionado
    '''

    def __init__(self, **kw):
        super().__init__(**kw)
        if kw.get('instance'):
            self.instance = kw.get('instance')

    def set_collection_info(self):

        if self.instance:
            collection = self.instance.collection_name
            version_collection = "{}_old".format(collection)
            unique = self.instance.unique

            return {'collection': collection, 'version_collection': version_collection,
                    'unique': unique, 'unique_str': self.instance.unique_str}

        return None

    def insert_or_version(self):

        info_db_dict = self.set_collection_info()
        try:
            element = self.client[info_db_dict['collection']].find_one(
                {info_db_dict['unique_str']: info_db_dict['unique']})
            if element:
                # existe en la bbdd
                print("elemento {} existente en la bbdd: {} -> {}".format(self.instance.__class__.__name__,
                                                                          info_db_dict['unique_str'],
                                                                          info_db_dict['unique']))
                # insertamos el documento en la coleccion de versionado, (old)
                print("Moviendo {} con id: {} a {}".format(self.instance.__class__.__name__,
                                                           element['_id'],
                                                           info_db_dict['version_collection']))

                element.update(
                    {'activo_hasta': str(datetime.now().replace(microsecond=0).isoformat().replace('T', ' '))})
                self.client[info_db_dict['version_collection']].insert_one(element)

                print("Borrando {} con id: {} a {}".format(self.instance.__class__.__name__,
                                                           element['_id'],
                                                           info_db_dict['version_collection']))
                self.client[info_db_dict['collection']].delete_one({'_id': ObjectId(element['_id'])})

            return self.client[info_db_dict['collection']].insert_one(self.instance.get_json()).inserted_id

        except Exception as e:
            print("Error en insert_or_version-> {}".format(e))

        return False


@property
def instance(self):
    # identificador univoco de la entidad
    return self._instance


@instance.setter
def instance(self, value):
    if issubclass(value.__class__, AireGas):
        self._instance = value
