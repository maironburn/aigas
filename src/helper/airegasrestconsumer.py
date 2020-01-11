import json
from common_config import ENDPOINT_URL
from logger.app_logger import AppLogger
import urllib3

print('Loading function')
url = "https://swapi.co/api/people"


class AiregasRestConsumer(object):
    _url = None
    _logger = None
    _http = None

    def __init__(self, **kwargs):

        self._logger = AppLogger.create_rotating_log() if not kwargs.get('logger') else kwargs.get('logger')
        self._logger.info("Iniciando {}".format(self.__class__.__name__))
        self.init_pool_request()

        self._url = kwargs.get('url') if kwargs and kwargs.get('url') else ENDPOINT_URL

    def init_pool_request(self):
        try:
            self._http = urllib3.PoolManager()
            self._logger.info("urllib3 request iniciado con exito")
            return True
        except Exception as e:
            self._logger.error("Error iniciando urllib3->{}".format(e))

        return None

    def test_connection_to_url(self):
        try:
            url_get = self._url if self._url else ENDPOINT_URL
            self.http.request('GET', url_get)
            self._logger.info("Connection to {} successful".format(url_get))
            return True
        except Exception as e:
            self._logger.error("Cannot connect to {}-> {}".format(url, e))

        return False



    def get_last_modifications_from_api_rest(self):
        try:
            r = self.http.request('GET', self.url)
            self._logger.info("Connection to {} successful".format(self.url))
            return json.loads(r.data.decode('utf-8'))
        except Exception as e:
            self._logger.error("Cannot connect to {}-> {}".format(url, e))

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if value:
            self._url = value

    @property
    def http(self):
        return self._http

    @http.setter
    def http(self, value):
        if value:
            self._http = value


