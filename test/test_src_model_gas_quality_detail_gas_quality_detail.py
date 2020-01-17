from mock import patch
import src.model.airegas_base
from src.model.airegas_base import AireGas
import src.model.atr_amount.atr_amount
from src.model.atr_amount.atr_amount import AireGas
from src.model.atr_amount.atr_amount import Atr_Amount
import src.model.atr_amount.atr_prices
from src.model.atr_amount.atr_prices import ATRPrices
import src.model.b70_calendar.b70_calendar
from src.model.b70_calendar.b70_calendar import AireGas
from src.model.b70_calendar.b70_calendar import B70_Calendar
import src.model.calendar.calendar
from src.model.calendar.calendar import AireGas
from src.model.calendar.calendar import Calendar
import src.model.calendar.periods
from src.model.calendar.periods import Periods
import src.model.cli.cli
from src.model.cli.cli import AireGas
from src.model.cli.cli import Cli
import src.model.cli.contract
from src.model.cli.contract import Contract
import src.model.cli.invoice
from src.model.cli.invoice import Invoice
import src.model.cli.supply
from src.model.cli.supply import Supply
import src.model.consumption.consumption
from src.model.consumption.consumption import AireGas
from src.model.consumption.consumption import Consumption
from src.model.forecast.forecast import Forecast
import src.model.gas_quality_detail.gas_quality_detail
from src.model.gas_quality_detail.gas_quality_detail import AireGas
from src.model.gas_quality_detail.gas_quality_detail import Gas_Quality_Detail
import src.model.night_consumption.night_consumption
from src.model.night_consumption.night_consumption import AireGas
from src.model.night_consumption.night_consumption import Night_Consumption
from src.model.nomination.nomination import Nomination
from src.model.regulated_price.regulated_price import Regulated_Price
import unittest


class Gas_quality_detailTest(unittest.TestCase):
    @patch.object(AireGas, 'get_json')
    def test_get_json(self, mock_get_json):
        mock_get_json.return_value = {'ts': '2020-01-16T13:10:44', 'calendarCode': 'CAL_BF_2020_EntreSemana', 'Periods': [{'idPeriod': '672', 'from': '2020-01-01', 'to': '2020-01-31', 'calendarDates': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31'], 'active': [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]}, {'idPeriod': '673', 'from': '2020-01-01', 'to': '2020-01-31', 'calendarDates': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31'], 'active': [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]}, {'idPeriod': '674', 'from': '2020-02-01', 'to': '2020-02-28', 'calendarDates': ['2020-02-01', '2020-02-02', '2020-02-03', '2020-02-04', '2020-02-05', '2020-02-06', '2020-02-07', '2020-02-08', '2020-02-09', '2020-02-10', '2020-02-11', '2020-02-12', '2020-02-13', '2020-02-14', '2020-02-15', '2020-02-16', '2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22', '2020-02-23', '2020-02-24', '2020-02-25', '2020-02-26', '2020-02-27', '2020-02-28', '2020-02-29'], 'active': [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]}]}
        gas_quality_detail_instance = Gas_Quality_Detail()
        self.assertEqual(
            gas_quality_detail_instance.get_json,
            {'ts': '2020-01-16T13:10:44', 'CLI': 'CLI001', 'date': ['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-03'], 'meter': ['meter1', 'meter2', 'meter1', 'meter2'], 'detailPCS': [1000, 2000, 3000, 2500], 'detailPCI': [1000, 2000, 3000, 2500], 'detailDensity': [1000, 2000, 3000, 2500], 'detailN2': [1000, 2000, 3000, 2500], 'detailPressure': [1000, 2000, 3000, 2500], 'detailTemp': [25, 26, 27, 26], 'detailValueZ': [1000, 2000, 3000, 2500], 'detailValueK': [1000, 2000, 3000, 2500], 'detailLectm3': [1000, 2000, 3000, 2500], 'detailConsm3': [1000, 2000, 3000, 2500], 'detailAdjustementskWh': [1000, 2000, 3000, 2500], 'detailConskWh': [1000, 2000, 3000, 2500], 'detailCO2': [1000, 2000, 3000, 2500]}
        )


    @patch.object(AireGas, 'load_data')
    def test_load_data(self, mock_load_data):
        mock_load_data.return_value = None
        gas_quality_detail_instance = Gas_Quality_Detail()
        self.assertEqual(
            gas_quality_detail_instance.load_data,
            None
        )


if __name__ == "__main__":
    unittest.main()
