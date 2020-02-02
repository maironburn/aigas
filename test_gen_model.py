from common_config import *
from src.helper.json_helper import get_entity_from_samples
from importlib import import_module
from src.model.calendar.calendar import Calendario
from src.model.b70_calendar.b70calendar import B70Calendar
from src.model.atr_amount.atramount import AtrAmount
from src.model.consumption.consumption import Consumption
from src.model.night_consumption.nightconsumption import NightConsumption
from src.model.cli.cli import Cli
from src.model.gas_quality_detail.gasqualitydetail import GasQualityDetail
from src.model.nomination.nomination import Nominacion
from src.model.formula_price.formula_price import PrecioFormula
from src.model.forecast.forecast import Forecast
from src.model.regulated_price.regulated_price import RegulatedPrice
from src.model.molecule_tax.molecule_tax import TasaMolecula
import auger

dict_instances = {'Calendar': Calendario,
                  'B70_Calendar': B70Calendar,
                  'Atr_Amount': AtrAmount,
                  'Consumption': Consumption,
                  'Night_Consumption': NightConsumption,
                  'Cli': Cli,
                  'Gas_Quality_Detail': GasQualityDetail,
                  'Nomination': Nominacion,
                  'Formula_Price': PrecioFormula,
                  'Forecast': Forecast,
                  'Regulated_Price': RegulatedPrice,
                  'Molecule_Tax': TasaMolecula
                  }


def main():
    module = import_module("common_config")

    for k, v in dict_instances.items():
        sample_file = getattr(module, "{}_SAMPLE".format(k.upper()))
        instance_data = get_entity_from_samples(sample_file)
        # instanciacion de la clase
        instance = v(**{'entity_data': instance_data})
        print(instance.get_json())


if __name__ == "__main__":
    with auger.magic([
        AtrAmount,
        B70Calendar,
        Calendario,
        Cli,
        Consumption,
        NightConsumption,
        GasQualityDetail,
        Nominacion,
        PrecioFormula,
        Forecast,
        RegulatedPrice,
        TasaMolecula
    ]):
        main()

