from src.model.airegas_base import AireGas


class Regulated_Price(AireGas):
    regulatedPriceName = None  # String
    regulatedDates = []  # Array<Date (ISO8601 (yyyy-MM-dd))>
    regulatedVal = []  # Array<Integer>

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.regulatedPriceName = self.json_entity_data['regulatedPriceName']
        self.regulatedDates = self.json_entity_data['regulatedDates']
        self.regulatedVal = self.json_entity_data['regulatedVal']

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "regulatedPriceName": self.regulatedPriceName,
            "regulatedDates": self.regulatedDates,
            "regulatedVal": self.regulatedVal,
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.regulatedPriceName
