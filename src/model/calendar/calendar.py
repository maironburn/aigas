from src.model.airegas_base import AireGas
from src.model.calendar.periods import Periods


class Calendario(AireGas):

    calendar_code = str
    Expiration_Date = str
    list_periods = []  # lista de periodos

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):

        super().load_data()
        self.calendar_code = self.json_entity_data['calendar_code']
        periods = self.json_entity_data['list_periods']
        periods and self.load_periods(periods)

    def load_periods(self, periods):
        print("Iniciando la carga de {} periodos asociados al calendar ".format(len(periods)))
        for p in periods:
            self.list_periods.append(Periods(**{'entity_data': p, 'logger': self._logger}))

        print("Instanciados {} periodos  ".format(len(self.list_periods)))

    def get_periods(self):

        periods = []
        for p in self.list_periods:
            periods.append(p.get_json())

        return periods

    # <editor-fold desc="getter and setters">
    def get_json(self):

        json_parent = AireGas.get_json(self)
        json_parent.update({
            "calendar_code": self.calendar_code,
            "list_periods": self.get_periods()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.calendar_code


    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "calendar_code"