from src.model.airegas_base import AireGas
from src.model.forecast.forecastdetails import ForecastDetails


class Forecast(AireGas):
    idContract = str
    unit = str
    prevision = {}

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.idContract = self.json_entity_data['idContract']

        prevision = self.json_entity_data["forecast"]
        prevision and self.load_prevision(prevision)

    def load_prevision(self, prevision):
        self.prevision = ForecastDetails(**{'entity_data': prevision, 'logger': self._logger})

    def get_prevision(self):
        return self.prevision.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "idContract": self.idContract,
            "unit": self.unit,
            "forecast": self.get_prevision()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.idContract

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "CLI"
