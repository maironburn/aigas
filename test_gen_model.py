from common_config import *
from src.helper.json_helper import get_entity_from_samples
from importlib import import_module
from src.model.calendar.calendar import Calendario
from src.model.b70_calendar.b70_calendar import B70_Calendar
from src.model.atr_amount.atr_amount import Atr_Amount
from src.model.consumption.consumption import Consumption
from src.model.night_consumption.night_consumption import Night_Consumption
from src.model.cli.cli import Cli
from src.model.gas_quality_detail.gas_quality_detail import Gas_Quality_Detail
from src.model.nomination.nomination import Nominacion
from src.model.formula_price.formula_price import PrecioFormula
from src.model.forecast.forecast import Forecast
from src.model.regulated_price.regulated_price import Regulated_Price
from src.model.molecule_tax.molecule_tax import TasaMolecula
import auger

dict_instances = {'Calendar': Calendario,
                  'B70_Calendar': B70_Calendar,
                  'Atr_Amount': Atr_Amount,
                  'Consumption': Consumption,
                  'Night_Consumption' : Night_Consumption,
                  'Cli' : Cli,
                  'Gas_Quality_Detail': Gas_Quality_Detail,
                  'Nomination' : Nominacion,
                  'Formula_Price' : PrecioFormula,
                  'Forecast' : Forecast,
                  'Regulated_Price' : Regulated_Price,
                  'Molecule_Tax' : TasaMolecula
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
     Atr_Amount,
     B70_Calendar,
     Calendario,
     Cli,
     Consumption,
     Night_Consumption,
     Gas_Quality_Detail,
     Nominacion,
     PrecioFormula,
     Forecast,
     Regulated_Price,
     TasaMolecula
 ]):   # this is the new line and invokes Auger
    main()