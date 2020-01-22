from src.model.airegas_base import AireGas
from src.model.atr_amount.atr_prices import ATRPrices

class Atr_Amount(AireGas):
    CLI = None  # String
    From = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    To = None  # DateTime (ISO8601 (yyyy-MM-ddThh:mm:ss))
    ATRPrices = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):

        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self.From = self.json_entity_data['From']
        self.To = self.json_entity_data['To']

        atr_prices = self.json_entity_data['ATRPrices']
        atr_prices and self.load_atr_prices(atr_prices)

    def load_atr_prices(self, atr_prices):
        self._logger.info(
            "Iniciando la carga de {} ATRPrices asociados a {} ".format(len(atr_prices), self.__class__.__name__))
        for atr in atr_prices:
            self.ATRPrices.append(ATRPrices(**{'entity_data': atr, 'logger': self._logger}))

        self._logger.info("Instanciados {} ATRPrices  ".format(len(self.ATRPrices)))

    def get_ATRPrices_json(self):

        atr_prices = []
        for atr in self.ATRPrices:
            atr_prices.append(atr.get_json())

        return atr_prices

    # <editor-fold desc="getter and setters">
    def get_json(self):

        json_parent = AireGas.get_json(self)
        json_parent.update({
            "CLI": self.CLI,
            "From": self.From,
            "To": self.To,
            "ATRPrices": self.get_ATRPrices_json()
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