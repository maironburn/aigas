from mock import patch
from src.model.regulated_price.regulated_price import AireGas
from src.model.regulated_price.regulated_price import Regulated_Price
import unittest


class Regulated_priceTest(unittest.TestCase):
    @patch.object(AireGas, 'get_json')
    def test_get_json(self, mock_get_json):
        mock_get_json.return_value = {'ts': '2020-01-16T13:10:44', 'calendarCode': 'CAL_BF_2020_EntreSemana', 'Periods': [{'idPeriod': '672', 'from': '2020-01-01', 'to': '2020-01-31', 'calendarDates': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31'], 'active': [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]}, {'idPeriod': '673', 'from': '2020-01-01', 'to': '2020-01-31', 'calendarDates': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31'], 'active': [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]}, {'idPeriod': '674', 'from': '2020-02-01', 'to': '2020-02-28', 'calendarDates': ['2020-02-01', '2020-02-02', '2020-02-03', '2020-02-04', '2020-02-05', '2020-02-06', '2020-02-07', '2020-02-08', '2020-02-09', '2020-02-10', '2020-02-11', '2020-02-12', '2020-02-13', '2020-02-14', '2020-02-15', '2020-02-16', '2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22', '2020-02-23', '2020-02-24', '2020-02-25', '2020-02-26', '2020-02-27', '2020-02-28', '2020-02-29'], 'active': [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]}]}
        regulated_price_instance = Regulated_Price()
        self.assertEqual(
            regulated_price_instance.get_json,
            {'ts': '2020-01-16T13:10:44', 'regulatedPriceName': 'Peaje', 'regulatedDates': ['2020-01-01', '2020-01-02', '2020-01-03'], 'regulatedVal': [1231, 6542, 41414]}
        )


    @patch.object(AireGas, 'load_data')
    def test_load_data(self, mock_load_data):
        mock_load_data.return_value = None
        regulated_price_instance = Regulated_Price()
        self.assertEqual(
            regulated_price_instance.load_data,
            None
        )


if __name__ == "__main__":
    unittest.main()
