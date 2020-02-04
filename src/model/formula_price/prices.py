import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class Prices(object):
    day = None
    formula_price = None
    formula_price_detail = None
    last_modified = None
    expiration_date = None

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self.load_data()

    def load_data(self):

        self.day = self.json_entity_data['day']
        self.formula_price = self.json_entity_data['formulaPrice']
        self.formula_price_detail = self.json_entity_data['formulaPriceDetail']
        self.last_modified = self.json_entity_data['lastModified']
        self.expiration_date = self.json_entity_data['expirationDate']

    def get_json(self):
        return {"day": self.day,
                "formulaPrice": self.formula_price,
                "formulaPriceDetail": self.formula_price_detail,
                "lastModified": self.last_modified,
                "expirationDate": self.expiration_date
                }
