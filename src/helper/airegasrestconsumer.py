import json
from common_config import ENDPOINT_URL
from logger.app_logger import AppLogger
import urllib3

print('Loading function')
url = "http://airegastestapp1.axpohosting.local:8081/"


class AiregasRestConsumer(object):
    _url = None
    _logger = None
    _http = None

    def __init__(self, **kwargs):
        self.init_pool_request()

        self._url = kwargs.get('url') if kwargs and kwargs.get('url') else ENDPOINT_URL

    def init_pool_request(self):
        try:
            self._http = urllib3.PoolManager()

            return True
        except Exception as e:
           print("Error iniciando urllib3->{}".format(e))

        return None

    def test_connection_to_url(self):
        try:
            url_get = self._url if self._url else ENDPOINT_URL
            self.http.request('GET', url_get)
            print("Connection to {} successful".format(url_get))
            return True
        except Exception as e:
            print("Cannot connect to {}-> {}".format(url, e))

        return False

    def get_last_modifications_from_api_rest(self, _from='2020-01-01'):
        try:

            r = self.http.request('GET', self.url, fields={'from': _from})
            print("Connection to {} successful".format(self.url))
            return json.loads(r.data.decode('utf-8'))
        except Exception as e:
            self._logger.error("Cannot connect to {}-> {}".format(self.url, e))

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
