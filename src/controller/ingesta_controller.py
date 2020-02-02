from common_config import ENDPOINT_URL
from src.mongodb.mongo_client import MongoAireGas
from src.helper.airegasrestconsumer import AiregasRestConsumer
from logger.app_logger import AppLogger


class IngestaController(object):
    _db_client = None
    _api_consumer = None
    _logger = None

    def __init__(self, **kw):
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')

        if kw.get('db_client') and kw.get('api_client'):
            self._db_client = kw.get('db_client')
            self._api_consumer = kw.get('api_client')

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
    mongo_airegas.connect_db()
    api_client = AiregasRestConsumer(**{'logger': mongo_airegas.logger})
    if mongo_airegas.client and api_client.test_connection_to_url():
        kwdata['db_client'] = mongo_airegas.client
        kwdata['api_client'] = api_client.http
        kwdata['logger'] = mongo_airegas.logger
        ingesta_controller = IngestaController(**kwdata)

    else:
        print("Can't initialize IngestaController")
