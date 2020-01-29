from pymongo import MongoClient
from logger.app_logger import AppLogger
from common_config import MONGODB_LOCAL, MONGODB_ATLAS


class MongoAireGas(object):
    _connection_string = None
    _db_name = str
    _host = str
    _port = str
    _user = str
    _password = str

    _client = None
    _logger = None

    def __init__(self, **kwargs):
        self._logger = AppLogger.create_rotating_log() if not kwargs.get('logger') else kwargs.get('logger')
        self._logger.info("Iniciando {}".format(self.__class__.__name__))
        # db_data = kwargs if kwargs and isinstance(kwargs, dict) else MONGODB_TESTl
        self.connection_string = MONGODB_LOCAL if kwargs.get('connection_type') == 'local' else MONGODB_ATLAS

    def connect_db(self, db_name='db_test'):
        try:
            mongo_con = MongoClient(self.connection_string)
            self._logger.info("connect_db: Succesful Connection ")
            self._client = mongo_con[db_name]
            return True

        except Exception as e:
            self._logger.error("Cant connect with Document DB ->{}".format(e))

        return False

    def insert_or_version(self):

        pass
        # coleccion = collection_mapper[k].lower()
        # inserted_id = mongo_client.client[coleccion].insert_one(
        #     instance_json).inserted_id
        # print("{}".format(inserted_id))

    def get_last_update(self):
        pass

    # <editor-fold desc="Getter/ Setters">

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        if value:
            self._logger = value

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, value):
        if value:
            self._db_name = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if value:
            self._host = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if value:
            self._port = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if value:
            self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value:
            self._password = value

    @property
    def client(self):
        # cliente de la bbdd
        return self._client

    @client.setter
    def client(self, value):
        # cliente de la bbdd
        if value:
            self._client = value

    @property
    def connection_string(self):
        # identificador univoco de la entidad
        return self._connection_string

    @connection_string.setter
    def connection_string(self, value):
        if value:
            self._connection_string = value

    # </editor-fold>
