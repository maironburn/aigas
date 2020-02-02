from src.model.airegas_base import AireGas


class GasQualityDetail(AireGas):
    CLI = ""
    date = []
    meter = []
    detailPCS = []
    detailPCI = []
    detailDensity = []
    detailN2 = []
    detailPressure = []
    detailTemp = []
    detailValueZ = []
    detailValueK = []
    detailLectm3 = []
    detailConsm3 = []
    detailAdjustementskWh = []
    detailConskWh = []
    detailCO2 = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self.date = self.json_entity_data['date']
        self.meter = self.json_entity_data['meter']
        self.detailPCS = self.json_entity_data['detailPCS']
        self.detailPCI = self.json_entity_data['detailPCI']
        self.detailDensity = self.json_entity_data['detailDensity']
        self.detailN2 = self.json_entity_data['detailN2']
        self.detailPressure = self.json_entity_data['detailPressure']
        self.detailTemp = self.json_entity_data['detailTemp']
        self.detailValueZ = self.json_entity_data['detailValueZ']
        self.detailValueK = self.json_entity_data['detailValueK']
        self.detailLectm3 = self.json_entity_data['detailLectm3']
        self.detailConsm3 = self.json_entity_data['detailConsm3']
        self.detailAdjustementskWh = self.json_entity_data['detailAdjustementskWh']
        self.detailConskWh = self.json_entity_data['detailConskWh']
        self.detailCO2 = self.json_entity_data['detailCO2']

    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "CLI": self.CLI,
            "date": self.date,
            "meter": self.meter,
            "detailPCS": self.detailPCS,
            "detailPCI": self.detailPCI,
            "detailDensity": self.detailDensity,
            "detailN2": self.detailN2,
            "detailPressure": self.detailPressure,
            "detailTemp": self.detailTemp,
            "detailValueZ": self.detailValueZ,
            "detailValueK": self.detailValueK,
            "detailLectm3": self.detailLectm3,
            "detailConsm3": self.detailConsm3,
            "detailAdjustementskWh": self.detailAdjustementskWh,
            "detailConskWh": self.detailConskWh,
            "detailCO2": self.detailCO2
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
