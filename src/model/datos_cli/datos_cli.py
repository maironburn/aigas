from src.model.datos_cli.contract import Contract
from src.model.datos_cli.invoice import Invoice
from src.model.datos_cli.supply import Supply
from src.model.airegas_base import AireGas


class DatosCLI(AireGas):
    CLI = None  # String
    StartDate = None  # Date (ISO8601 (yyyy-MM-dd))
    EndDate = None  # Date (ISO8601 (yyyy-MM-dd))
    invoice = {}
    supply = {}
    contract = {}

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = False

    def load_data(self):
        super().load_data()
        self.CLI = self.json_entity_data['CLI']
        self.StartDate = self.json_entity_data['StartDate']
        self.EndDate = self.json_entity_data['EndDate']

        invoice = self.json_entity_data['invoice']
        supply = self.json_entity_data['supply']
        contract = self.json_entity_data['contract']

        invoice and self.load_invoice(invoice)
        supply and self.load_supply(supply)
        contract and self.load_contract(contract)

    def load_invoice(self, invoice):
        self.invoice = Invoice(**{'entity_data': invoice, 'logger': self._logger})


    def load_supply(self, supply):
        self.supply = Supply(**{'entity_data': supply, 'logger': self._logger})


    def load_contract(self, contract):
        self.contract = Contract(**{'entity_data': contract, 'logger': self._logger})


    def get_invoice(self):
        return self.invoice.get_json()

    def get_supply(self):
        return self.supply.get_json()

    def get_contract(self):
        return self.contract.get_json()

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)
        json_parent.update({
            "CLI": self.CLI,
            "StartDate": self.StartDate,
            "EndDate": self.EndDate,
            "invoice": self.get_invoice(),
            "supply": self.get_supply(),
            "contract": self.get_contract()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.CLI
