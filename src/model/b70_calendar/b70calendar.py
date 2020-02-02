from src.model.airegas_base import AireGas


class B70Calendar(AireGas):
    CLI = None
    From = None
    To = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self.From = self.json_entity_data['from']
        self.To = self.json_entity_data['to']

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "CLI": self.CLI,
            "from": self.From,
            "to": self.To,
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.CLI
