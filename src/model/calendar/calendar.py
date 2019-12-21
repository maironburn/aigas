from src.model.airegas_base import AireGas
from src.model.calendar.periods import Periods


class Calendar(AireGas):
    calendarCode = None  # String
    periods = []  # lista de periodos

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):

        super().load_data()
        self.calendarCode = self.json_entity_data['calendarCode']
        periods = self.json_entity_data['Periods']
        periods and self.load_periods(periods)

    def load_periods(self, periods):
        self._logger.info("Iniciando la carga de {} periodos asociados al calendar ".format(len(periods)))
        for p in periods:
            self.periods.append(Periods(**{'entity_data': p, 'logger': self._logger}))

        self._logger.info("Instanciados {} periodos  ".format(len(self.periods)))

    def get_periods(self):

        periods = []
        for p in self.periods:
            periods.append(p.get_json())

        return periods

    # <editor-fold desc="getter and setters">
    def get_json(self):

        json_parent = AireGas.get_json(self)
        json_parent.update({
            "calendarCode": self.calendarCode,
            "Periods": self.get_periods()
        })
        return json_parent

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.calendarCode

