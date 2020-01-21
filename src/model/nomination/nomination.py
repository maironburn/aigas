from src.model.airegas_base import AireGas
from src.model.nomination.nomination_details import Nomination_Details


class Nominacion(AireGas):
    CLI = None  # String
    nomination = {}  # segun modelo funcional es un objeto y no una matriz, e.d, relacion 1:1
    _cli = str

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self._cli = self.json_entity_data['cli']
        nomination = self.json_entity_data['nomination']

        nomination and self.load_nomination(nomination)

    def load_nomination(self, nomination):
        self._logger.info(
            "Iniciando la carga del objeto nomination asociada a {} ".format(self.__class__.__name__))
        self.nomination = Nomination_Details(**{'entity_data': nomination, 'logger': self._logger})

    def get_nomination(self):
        return self.nomination.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "CLI": self.CLI,
            "nomination": self.get_nomination()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.CLI
