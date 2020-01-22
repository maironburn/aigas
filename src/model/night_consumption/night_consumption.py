from src.model.airegas_base import AireGas


class Night_Consumption(AireGas):
    CLI = None  # String
    dates = None  # Array<Date (ISO8601 (yyyy-MM-dd))>
    origin = None  # Array<String>
    qd = None  # Array<Integer>

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self.dates = self.json_entity_data['dates']
        self.origin = self.json_entity_data['origin']
        self.qd = self.json_entity_data['qd']

    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "CLI": self.CLI,
            "dates": self.dates,
            "origin": self.origin,
            "qd": self.qd
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