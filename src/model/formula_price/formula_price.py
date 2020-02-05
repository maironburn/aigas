from src.model.airegas_base import AireGas
from src.model.formula_price.prices import Prices


class PrecioFormula(AireGas):
    formula_code = None
    formula_des = None
    currency = None
    unit = None
    compound_index = None
    daily_detail = []

    divisa = str

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.formula_code = self.json_entity_data['formulaCode']
        self.formula_des = self.json_entity_data['formulaDes']
        self.currency = self.json_entity_data['currency']
        self.unit = self.json_entity_data['unit']
        self.compound_index = self.json_entity_data['compoundIndex']
        daily_detail = self.json_entity_data['dailyDetail']
        daily_detail and self.load_prices(daily_detail)

    def load_prices(self, prices):
        for p in prices:
            self.daily_detail.append(Prices(**{'entity_data': p}))

    def get_prices(self):

        details = []
        for n in self.daily_detail:
            details.append(n.get_json())

        return details

    # <editor-fold desc="getter and setters">

    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "formulaCode": self.formula_code,
            "formulaDes": self.formula_des,
            "currency": self.currency,
            "unit": self.unit,
            "compoundIndex": self.compound_index,
            "dailyDetail": self.get_prices()
        })
        return json_parent

    def get_collection_db_info(self):
        collection_info_base = AireGas.get_collection_db_info(self)
        collection_info_base.update({

            "unique": self.formula_code,
            "unique_str": "formulaCode",
            "last": "maxLastModified"
        })

        return collection_info_base

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.formula_code

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "formulaCode"
