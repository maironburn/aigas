from pymongo import MongoClient
from common_config import MONGODB_TEST
from logger.app_logger import AppLogger


class MongoAireGas(object):
    _connection_string = None
    _db_name = None
    _host = None
    _port = None

    _client = None
    _logger = None

    def __init__(self, **kwargs):
        self._logger = AppLogger.create_rotating_log() if not kwargs.get('logger') else kwargs.get('logger')
        self._logger.info("Iniciando {}".format(self.__class__.__name__))
        db_data = kwargs if kwargs and isinstance(kwargs, dict) else MONGODB_TEST
        self.load_data_for_string_connection(db_data)
        self._client = self.connect_db()

    def load_data_for_string_connection(self, kwargs):

        self._logger.info("Loading data to build string connection")
        self.db_name = kwargs.get('db_name')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')

        self._logger.info("DB_NAME : {} , HOST: {}, PORT: {}".format(self.db_name,
                                                                     self.host,
                                                                     self.port))

    def connect_db(self):

        if self.db_name:
            '''
            #test db no auth  
            # cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
            '''
            self._client = MongoClient("mongodb://{}:{}".format(self.host, self.port))
            self._logger.info("connect_db: Succesful Connection ")
            return self._client[self.db_name]

        self._logger.error("connect_db: No succesful connection ")
        return None

    def get_last_update(self):

        """
        funcion que recupera la fecha de la ultima actualizacion de la entidad
        para despues consumir en el api rest de airegas

        db.calendar.where("_id").eq("2020010100001").limit(100)
        db.calendar.find().max(ts)
        db.calendar.find( ,{max(ts):1} )
            """
        pass

    # <editor-fold desc="Getter/ Setters">

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
            pass

    # </editor-fold>
