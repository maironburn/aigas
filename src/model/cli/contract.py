import json

from logger.app_logger import AppLogger
from src.helper.common_helper import check_field_integrity


class Contract(object):
    counter_party_name = None  # String
    counter_party_doc_number = None  # String
    client_name = None  # String
    connection_point = []  # String
    start_date = []  # String
    active = None  # Integer
    portfolio = None  # String
    broker = None  # String
    commission = None  # Double


    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self.counter_party_name = self.json_entity_data['CounterPartyName']
            self.counter_party_doc_number = self.json_entity_data['CounterPartyDocNumber']
            self.client_name = self.json_entity_data['clientName']
            self.connection_point = self.json_entity_data['connectionPoint']
            self.start_date = self.json_entity_data['startDate']
            self.active = self.json_entity_data['active']
            self.portfolio = self.json_entity_data['portfolio']
            self.broker = self.json_entity_data['broker']
            self.commission = self.json_entity_data['commission']

        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"CounterPartyName": self.counter_party_name,
                "CounterPartyDocNumber": self.counter_party_doc_number,
                "clientName": self.client_name,
                "connectionPoint": self.connection_point,
                "startDate": self.start_date,
                "active": self.active,
                "portfolio": self.portfolio,
                "broker": self.broker,
                "commission": self.commission
                }
