from src.mongodb.mongo_client import MongoAireGas
from src.model.airegas_base import AireGas
from datetime import datetime
from bson.objectid import ObjectId
from datetime import datetime
from datetime import timedelta
from src.helper.common_helper import get_date_from_string


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
            _from = self.instance.From
            _to = self.instance.To
            return {'collection': collection, 'version_collection': version_collection,
                    'unique': unique, 'unique_str': self.instance.unique_str, 'from': _from, 'to': _to}

        return None

    def insert_or_version(self):

        info_db_dict = self.instance.get_collection_db_info()
        try:
            element = self.client[info_db_dict['collection']].find_one(
                {info_db_dict['unique_str']: info_db_dict['unique']})
            kw = {'current': element, 'info_db_dict': info_db_dict}

            if element:
                print("iniciando proceso de versionado")
                self.standard_version_proc(**kw)

            inserted_id = self.client[info_db_dict['collection']].insert_one(self.instance.get_json()).inserted_id
            print(
                "Insercion en Document DB, coleccion: {} , unnique: {}, id: {}".format(self.instance.__class__.__name__,
                                                                                       self.instance.unique,
                                                                                       inserted_id))

            return inserted_id

        except Exception as e:
            print("Error en insert_or_version-> {}".format(e))

        return False

    # def logica_tasa_molecula(self, current_db_tax, info_db_dict):
    def logica_tasa_molecula(self, **kw):
        current_db_tax = kw.get('current')
        info_db_dict = kw.get('info_db_dict')

        for doc_in_db in list(current_db_tax):

            if self.tm_are_equal(doc_in_db):
                return self.standard_version_proc(doc_in_db, info_db_dict, {
                    info_db_dict['unique_str']: info_db_dict['unique'],
                    'from': current_db_tax['from']})
            else:
                incoming_instance_from = get_date_from_string(self.instance.From.split()[0])
                incoming_instance_to = get_date_from_string(self.instance.To)

                from_doc_in_db = get_date_from_string(doc_in_db['from'])
                to_doc_in_db = get_date_from_string(doc_in_db['to'])

                if doc_in_db['to'] == None and incoming_instance_from > from_doc_in_db:
                    print(
                        "instance_from: {} > current_doc from: {}".format(incoming_instance_from, from_doc_in_db))
                    # en el doc existente se actualiza el "to" con el from del incoming - 1 dia
                    print("current before update : {}".format(doc_in_db))
                    doc_in_db['to'] = incoming_instance_from - timedelta(days=1)
                    print("elemnet is gonna be updated to : {}".format(doc_in_db))
                    self.client[info_db_dict['collection']].update_one({'_id': ObjectId(doc_in_db['_id'])},
                                                                       {'$set': {'to': str(doc_in_db['to'])}})
                    print("update done, taxCode: {}".format(doc_in_db['taxCode']))

                elif doc_in_db['to'] != None and incoming_instance_from > to_doc_in_db:
                    pass

    def tm_are_equal(self, current_in_db):

        return self.instance.From == current_in_db['from'] and self.instance.To == current_in_db['to']

    # def standard_version_proc(self, current, info_db_dict, **delete_condition_kw):
    def standard_version_proc(self, **kw):

        current = kw.get('current')
        info_db_dict = kw.get('info_db_dict')
        delete_condition_kw = kw.get('delete_condition_kw', {info_db_dict['unique_str']: info_db_dict['unique']})

        # insertamos el documento en la coleccion de versionado, (old)
        print("Moviendo {} con id: {} a {}".format(self.instance.__class__.__name__,
                                                   current['_id'],
                                                   info_db_dict['version_collection']))

        current.update(
            {'activo_hasta': str(datetime.now().replace(microsecond=0).isoformat().replace('T', ' '))})
        self.client[info_db_dict['version_collection']].insert_one(current)

        print("Borrando {} con id: {} de {}".format(self.instance.__class__.__name__,
                                                    current['_id'],
                                                    info_db_dict['collection']))

        result = self.client[info_db_dict['collection']].delete_one(delete_condition_kw)
        print("deleted_count : {}".format(result.deleted_count))

    def tasa_molec_version(self):

        info_db_dict = self.set_collection_info()
        try:
            # la consulta puede devolver uno o varios documentos
            element = self.client[info_db_dict['collection']].find(
                {info_db_dict['unique_str']: info_db_dict['unique']})

            if element.count():
                print("Existen tasas con el mismo taxCode {} en BBDD".format(info_db_dict['unique']))
                self.logica_tasa_molecula(element[:], info_db_dict)
                return True

        except Exception as e:
            print("Error en insert_or_version-> {}".format(e))

        return False

    def check_max_last_modified(self, last='maxLastModified'):
        info_db_dict = self.instance.get_collection_db_info()
        dict_document = self.client[info_db_dict['collection']].find_one(sort=[(info_db_dict['last'], -1)])
        if dict_document:
            print("document with max ({}) value: {}".format(last, dict_document))
            return dict_document[last]

        return None

    @property
    def instance(self):
        # identificador univoco de la entidad
        return self._instance

    @instance.setter
    def instance(self, value):
        if issubclass(value.__class__, AireGas):
            self._instance = value
