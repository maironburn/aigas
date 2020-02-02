import json

from logger.app_logger import AppLogger
from src.helper.json_helper import check_field_integrity


class ATRPrices(object):
    tpa_id = None  # String
    tpa_concept = None  # String
    tpa_concept_amount = None  # Integer

    _logger = None
    json_entity_data = None

    def __init__(self, **kw):

        self.json_entity_data = kw.get('entity_data', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger') else kw.get('logger')
        self.load_data()

    def load_data(self):
        self._logger.info("Checking fields from entity {}".format(self.__class__.__name__))

        if check_field_integrity("{}_FIELDS".format(self.__class__.__name__), self.json_entity_data):
            self.tpa_id = self.json_entity_data['TPAId']
            self.tpa_concept = self.json_entity_data['TPAConcept']
            self.tpa_concept_amount = self.json_entity_data['TPAConceptAmount']
        else:
            self._logger.error("{} faltan campos en {}".format(self.__class__.__name__,
                                                               json.dumps(self.json_entity_data)))

    def get_json(self):

        return {"TPAId": self.tpa_id,
                "TPAConcept": self.tpa_concept,
                "TPAConceptAmount": self.tpa_concept_amount
                }
