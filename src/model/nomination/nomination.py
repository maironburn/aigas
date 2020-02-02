from src.model.airegas_base import AireGas
from src.model.nomination.nomination_details import NominationDetails


class Nominacion(AireGas):

    idContract = str
    nominations = {}
    unit = str

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.idContract = self.json_entity_data['idContract']
        self.unit = self.json_entity_data['unit']

        nominations = self.json_entity_data['nominations']

        nominations and self.load_nomination(nominations)

    def load_nominations(self, nominations):
        # self._logger.info(
        #     "Iniciando la carga del objeto nomination asociada a {} ".format(self.__class__.__name__))
        self.nominations = Nomination_Details(**{'entity_data': nominations, 'logger': self._logger})

    def get_nomination(self):
        return self.nominations.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "idContract": self.idContract,
            "nominations": self.get_nomination()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.idContract

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "idContract"
