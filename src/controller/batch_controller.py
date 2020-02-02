from src.helper.aws_helper import *
from src.model.airegas_base import AireGas
from src.helper.json_helper import valid_date
from src.controller.mongo_contoller import MongoVersionController


class BatchController(object):
    _bucket_name = None
    _key = None
    _collection = None
    _json_masivo = {}
    _mongo_version_controller = MongoVersionController

    def __init__(self, **kwargs):

        self.bucket = kwargs.get('bucket')
        self.key = kwargs.get('key')
        self.collection = kwargs.get('collection')

    def is_informated_collection(self, collection):
        return ''.join(map(lambda x: x.strip(), collection.values())) != ''

    def check_if_carga_masiva(self):
        '''
        Comprueba si existe el fichero de carga masiva (modo de incio manual)
        En caso de existir comprueba si la colleccion esta informada ,
        e.d, tiene algún valor para :from, to, lastModified, toLastModified o ListCode
        :return: boolean
        si True:  modo carga masiva
        si False: modo delta
        '''
        if check_bucket_exists(self.bucket):
            self.json_masivo = read_s3_bucket(self.bucket, self.key)
            if self.json_masivo and self.collection.__name__ in self.json_masivo.keys():
                return self.is_informated_collection(self.json_masivo[self.collection.__name__])

        return False

    def process_data_carga_masiva(self):
        '''

        Procedemnte de la lectura del son de carga masiva, lee el diccionario correspondiente asociado a la coleccion y
        procesa los datos para darle el formato adecuado de cara a la posterior construccion de la query para
        consumir la API de airegas
        :return:
        '''
        processed_json = {}
        # json_masivo = read_s3_bucket(self.bucket, self.key)

        for k, v in self.json_masivo[self.collection.__name__].items():
            if k.lower() in ['from', 'to'] and len(v.split()) and valid_date(v.split()[0]):
                processed_json.update({k: v.split()[0]})  # date
            elif k.lower() == 'listcode' and len(v.split()):
                processed_json.update({k: v.split()})
            elif k.lower() in ['fromlastmodified', 'tolastmodified']:
                processed_json.update({k: v})  # datetime
        return processed_json

        # <editor-fold desc="getter/setters">

    @property
    def bucket(self):
        return self._bucket_name

    @bucket.setter
    def bucket(self, value):
        if value:
            self._bucket_name = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if value:
            self._key = value

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):

        if issubclass(value, AireGas):
            self._collection = value

    @property
    def json_masivo(self):
        return self._json_masivo

    @json_masivo.setter
    def json_masivo(self, value):
        if value:
            self._json_masivo = value

    # </editor-fold>
