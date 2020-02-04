from src.model.airegas_base import AireGas
from src.model.forecast.forecastdetails import ForecastDetails


class Prevision(AireGas):
    idContract = None
    unit = None
    prevision = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.idContract = self.json_entity_data['idContract']
        self.unit = self.json_entity_data['unit']
        forecast = self.json_entity_data["forecast"]
        forecast and self.load_prevision_details(forecast)

    def load_prevision_details(self, prevision_details):

        for p in prevision_details:
            self.prevision.append(ForecastDetails(**{'entity_data': p}))

    def get_prevision(self):

        previsions = []
        for n in self.prevision:
            previsions.append(n.get_json())

        return previsions

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
        return "idContract"
