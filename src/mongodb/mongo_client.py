from pymongo import MongoClient


class MongoGas(object):
    _connection_string = None
    _db_name = None
    _host = None
    _port = None

    _client = None

    def __init__(self, **kwargs):

        if kwargs and isinstance(kwargs, dict):
            self.db_name = kwargs.get('db_name')
            self.host = kwargs.get('host')
            self.port = kwargs.get('port')

            self.get_connection_string()

    def connect_db(self, **kwargs):

        if self.db_name:
            '''
            #test db no auth  
            # cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
            '''

            self._client = MongoClient("mongodb://{}:{}".format(self.host, self.port))

            return self._client[self.db_name]

        return None

    def get_last_update(db):
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
