from src.model.airegas_base import AireGas
from src.model.forecast.forecast_details import Forecast_Details


class Forecast(AireGas):
    CLI = str
    _cli = str
    unidad = str
    prevision = {}  # segun modelo funcional es un objeto y no una matriz, e.d, relacion 1:1

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        prevision = self.json_entity_data["prevision"]
        prevision and self.load_prevision(prevision)

    def load_prevision(self, prevision):
        self.prevision = Forecast_Details(**{'entity_data': prevision, 'logger': self._logger})

    def get_prevision(self):
        return self.prevision.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "CLI": self.CLI,
            "prevision": self.get_prevision()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.CLI

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "CLI"
