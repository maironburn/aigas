from src.model.airegas_base import AireGas


class TasaMolecula(AireGas):
    taxCode = None
    taxDes = None
    From = None
    To = None
    taxVal = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.taxCode = self.json_entity_data['taxCode']
        self.taxDes = self.json_entity_data['taxDes']
        self.From = self.json_entity_data['from']  # aaray
        self.To = self.json_entity_data['to']
        self.taxVal = self.json_entity_data['taxVal']  # aaray

    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "taxCode": self.taxCode,
            "taxDes": self.taxDes,
            "from": self.From,
            "to": self.To,
            "taxVal": self.taxVal

        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.taxCode

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "taxCode"
