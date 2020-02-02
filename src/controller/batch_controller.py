from src.helper.aws_helper import *
from src.model.airegas_base import AireGas
from src.helper.json_helper import valid_date
from src.controller.mongo_contoller import MongoVersionController
from src.controller.ingesta_controller import AiregasRestConsumer


class BatchController(object):
    _bucket_name = None
    _key = None
    _instance = None
    _json_masivo = {}
    _mongo_version_controller = None
    _end_point_api = None

    def __init__(self, **kwargs):

        self.bucket = kwargs.get('bucket')
        self.key = kwargs.get('key')
        self.instance = kwargs.get('instance')
        self.mongo_controller = kwargs.get('mongo_version_controller')
        self.end_point_api = kwargs.get('AIREGAS_ENDPOINT_URL')

    @staticmethod
    def is_informated_collection(collection):
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
            if self.json_masivo and self.instance.__name__ in self.json_masivo.keys():
                return BatchController.is_informated_collection(self.json_masivo[self.instance.__name__])

        return False

    def process_data_carga_masiva(self):
        '''

        Procedemnte de la lectura del son de carga masiva, lee el diccionario correspondiente asociado a la coleccion y
        procesa los datos para darle el formato adecuado de cara a la posterior construccion de la query para
        consumir la API de airegas
        :return:
        '''
        processed_json = {}

        for k, v in self.json_masivo[self.instance.__name__].items():
            if k.lower() in ['from', 'to'] and len(v.split()) and valid_date(v.split()[0]):
                processed_json.update({k: v.split()[0]})  # date
            elif k.lower() == 'listcode' and len(v.split()):
                processed_json.update({k: v.split()})
            elif k.lower() in ['fromlastmodified', 'tolastmodified']:
                processed_json.update({k: v})  # datetime
        return processed_json

        # <editor-fold desc="getter/setters">

    def do_massive_procedure(self):

        # se procesan los datos del json de carga masiva relativos a la colleccion que entra como argumento
        data_to_build_query = self.process_data_carga_masiva()
        url = "{}/{}".format(self.end_point_api, self.instance.__name__)
        # construccion de la query para consumir de AireGas
        rest_consumer = AiregasRestConsumer(**{'url': url})
        response = rest_consumer.query_for_api_rest(**data_to_build_query)
        self.run_proccess_response_from_api(response, url)

    def do_delta_procedure(self):

        collection_entity = self.instance()
        self.mongo_controller.instance = collection_entity
        last_modified = self.mongo_controller.check_max_last_modified()
        url = "{}/{}".format(self.end_point_api, self.instance.__name__)
        rest_consumer = AiregasRestConsumer(**{'url': url})
        response = rest_consumer.query_for_api_rest(**{'fromLastModified': last_modified})

        self.run_proccess_response_from_api(response, url)

    def run_proccess_response_from_api(self, response, url):

        if isinstance(response, list):
            # insercion de DocumentDB de la coleccion recuperada del API
            for elements in response:
                collection_entity = self.instance(**{'entity_data': elements})
                self.mongo_controller.instance = collection_entity
                inserted_id = self.mongo_controller.insert_or_version()

                print("Insercion en Document DB, coleccion: {} , id: {}".format(self.instance.__name__, inserted_id))

        else:
            print("Error al acceder a la API, url: {}".format(url))

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
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, value):

        if issubclass(value, AireGas):
            self._instance = value

    @property
    def json_masivo(self):
        return self._json_masivo

    @json_masivo.setter
    def json_masivo(self, value):
        if value:
            self._json_masivo = value

    @property
    def mongo_controller(self):
        return self._mongo_version_controller

    @mongo_controller.setter
    def mongo_controller(self, value):
        if value:
            self._mongo_version_controller = value

    # </editor-fold>
