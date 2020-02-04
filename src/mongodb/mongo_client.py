from pymongo import MongoClient
from logger.app_logger import AppLogger


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
        self.connection_string = kwargs.get('DOCUMENTDB_URL')
        self.db_name = kwargs.get('DATABASE')

    def connect_db(self):
        try:
            mongo_con = MongoClient(self.connection_string)
            self._logger.info("connect_db: Succesful Connection ")
            self.client = mongo_con[self.db_name]
            return True

        except Exception as e:
            self._logger.error("Cant connect with Document DB ->{}".format(e))

        return False

    def database_exist(self, dbname):

        if self.mongo_con:
            dbnames = self.mongo_con.list_database_names()
            if dbname in dbnames:
                return True
        return False

    def collection_exists(self, collection_name):

        return collection_name in self.db_name.list_collection_names()

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
