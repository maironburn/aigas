from src.model.calendar.calendar import Calendar
from src.model.b70_calendar.b70_calendar import B70_Calendar
from src.model.atr_amount.atr_amount import Atr_Amount
from src.model.consumption.consumption import Consumption
from src.model.night_consumption.night_consumption import Night_Consumption
from src.model.cli.cli import CLI
from src.model.gas_quality_detail.gas_quality_detail import Gas_Quality_Detail
from src.model.nomination.nomination import Nomination
from src.model.formula_price.formula_price import Formula_Price
from src.model.forecast.forecast import Forecast
from src.model.regulated_price.regulated_price import Regulated_Price
from src.model.molecule_tax.molecule_tax import Molecule_Tax

from src.helper.airegas_rest import get_last_modifications_from_api_rest
import sys

dict_instances = {'Calendar': Calendar, 'B70_Calendar': B70_Calendar}

if __name__ == '__main__':

   # @todo
   # 1 - consulta en documentDB ( para la entidad que corresponda) max(ts)
   # 2 - construccion de la url para consumir la entidad del API REST adding el campo from
   # 3 - consumo API Rest de la entidad
   # 4 - instanciacion de la entidad from json
   # 5 - validacion de campos e integridad del response
   # 6 - Logica de versionado
   # 7 - insercion/es nombre_coleccion /nombre_coleccion_old


    print("the script has the name %s" % (sys.argv[0]))
    print("{}", format(get_last_modifications_from_api_rest(None, None)))
