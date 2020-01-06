from common_config import MONGODB_TEST, ENDPOINT_URL
from src.mongodb.mongo_client import MongoAireGas
from src.helper.api_airegas_client import Api_AireGas_Client
from logger.app_logger import AppLogger


class IngestaController(object):


    """
    # @todo
    # 1 - consulta en documentDB ( para la entidad que corresponda) max(ts)
    # 2 - construccion de la url para consumir la entidad del API REST adding el campo from
    # 3 - consumo API Rest de la entidad
    # 4 - instanciacion de la entidad from json
    # 5 - validacion de campos e integridad del response
    # 6 - Logica de versionado
    # 7 - insercion/es nombre_coleccion /nombre_coleccion_old
    """
    _db_client = None
    _api_consumer = None
    _logger  = None

    def __init__(self, **kw):
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')

        if kw.get ('db_client') and kw.get ('api_consumer'):
            self._db_client = kw.get('db_client')
            self._api_consumer = kw.get('api_consumerapi_consumer')

    @property
    def db_client(self):
        return self._db_client

    @db_client.setter
    def db_client(self, value):
        if value:
            self._db_client = value

    @property
    def api_consumer(self):
        return self._api_consumer

    @api_consumer.setter
    def api_consumer(self, value):
        if value:
            self._api_consumer = value


if __name__ == '__main__':

    kwdata = {'db_client': None, 'api_client': None}
    mongo_airegas = MongoAireGas()
    api_client = Api_AireGas_Client()
    if mongo_airegas.connect_db() and api_client.test_connection_to_url():
        kwdata['db_client'] = mongo_airegas.connect_db()
        kwdata['api_client'] = api_client.http
        ingesta_controller = IngestaController(**kwdata)

    else:
        print("Can't initialize IngestaController")