from src.model.airegas_base import AireGas
from src.model.formula_price.prices import Prices


class PrecioFormula(AireGas):
    formulaCode = None  # String
    formulaDes = None  # String
    From = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    To = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    compoundIndex = []  # Array<String>
    unidad = str
    divisia = str
    prices = {}  # segun modelo funcional es un objeto y no una matriz, e.d, relacion 1:1

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.formulaCode = self.json_entity_data['formulaCode']
        self.formulaDes = self.json_entity_data['formulaDes']
        self.From = self.json_entity_data['from']
        self.To = self.json_entity_data['to']
        self.compoundIndex = self.json_entity_data['compoundIndex']
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
            "formulaCode": self.formulaCode,
            "formulaDes": self.formulaDes,
            "from": self.From,
            "to": self.To,
            "compoundIndex": self.compoundIndex,
            "prices": self.get_prices()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.formulaCode
