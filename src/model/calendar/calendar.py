from logger.app_logger import AppLogger
from src.model.calendar.periods import Periods
from common_config import Calendar_FIELDS, PERIODS_FIELDS
from src.helper.json_helper import check_field_integrity
from src.model.airegas_base import AireGas
from datetime import datetime


class Calendar(AireGas):
    calendarCode = None  # String
    periods = []  # lista de periodos

    def __init__(self, **kw):

        super().__init__(**kw)

    def load_data(self):

        super().load_data()

        self._logger.info("Comprobando la integridad de la entidad {}".format(self.__class__.__name__))
        if check_field_integrity(Calendar_FIELDS, self.entity_data):
            self.calendarCode = self.entity_data['calendarCode']
            periods = self.entity_data['Periods']

            periods and self.load_periods(periods)

    def load_periods(self, periods):
        self._logger.info("Iniciando la carga de {} periodos asociados al calendar ".format(len(periods)))
        for p in periods:
            if check_field_integrity(PERIODS_FIELDS, p):
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
