import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Invoice(object):
    email = None  # String
    name = None  # String
    IBAN = None  # String
    swift = None  # String
    paymentTerm = None  # String
    paymentMethod = None  # String

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self.email = self.json_entity_data['email']
            self.name = self.json_entity_data['name']
            self.IBAN = self.json_entity_data['IBAN']
            self.swift = self.json_entity_data['swift']
            self.paymentTerm = self.json_entity_data['paymentTerm']
            self.paymentMethod = self.json_entity_data['paymentMethod']

        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"email": self.email,
                "name": self.name,
                "IBAN": self.IBAN,
                "swift": self.swift,
                "paymentTerm": self.paymentTerm,
                "paymentMethod": self.paymentMethod
                }
