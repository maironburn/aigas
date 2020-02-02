from src.model.airegas_base import AireGas
from src.model.formula_price.prices import Prices


class PrecioFormula(AireGas):
    formula_code = None
    formula_des = None
    _from = None
    _to = None
    compound_index = []
    unidad = str
    divisa = str
    prices = {}

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.formula_code = self.json_entity_data['formulaCode']
        self.formula_des = self.json_entity_data['formulaDes']
        self._from = self.json_entity_data['from']
        self._to = self.json_entity_data['to']
        self.compound_index = self.json_entity_data['compoundIndex']
        prices = self.json_entity_data["prices"]

        prices and self.load_prices(prices)

    def load_prices(self, prices):
        self._logger.info(
            "Iniciando la carga de {} prices asociados a {} ".format(len(prices), self.__class__.__name__))
        self.prices = Prices(**{'entity_data': prices, 'logger': self._logger})

    def get_prices(self):
        return self.prices.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "formulaCode": self.formula_code,
            "formulaDes": self.formula_des,
            "from": self._from,
            "to": self._to,
            "compoundIndex": self.compound_index,
            "prices": self.get_prices()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.formula_code


    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "formulaCode"
