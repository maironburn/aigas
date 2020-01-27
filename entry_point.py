from src.helper.json_helper import get_entity_from_samples
from src.mongodb.mongo_client import MongoAireGas
from common_config import *
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
from src.helper.airegasrestconsumer import AiregasRestConsumer
from src.controller.mongo_contoller import MongoVersionController
import time
import sys

dict_instances = {'Calendario': Calendario,
                  # 'B70_Calendar': B70_Calendar,
                  # 'Atr_Amount': Atr_Amount,
                  # 'Consumption': Consumption,
                  # 'Night_Consumption': Night_Consumption,
                  # 'Cli': Cli,
                  # 'Gas_Quality_Detail': Gas_Quality_Detail,
                  # 'Nominacion': Nominacion,
                  # 'Formula_Price': PrecioFormula,
                  # 'Forecast': Forecast,
                  # 'Regulated_Price': Regulated_Price,
                  'TasaMolecula': TasaMolecula
                  }

# mapea las clases con sus colecciones en MongoDB para la persistencia


if __name__ == '__main__':
    # @todo
    # 1 - consulta en documentDB ( para la entidad que corresponda) max(ts)
    # 2 - construccion de la url para consumir la entidad del API REST adding el campo from
    # 3 - consumo API Rest de la entidad
    # 4 - instanciacion de la entidad from json
    # 5 - validacion de campos e integridad del response
    # 6 - Logica de versionado
    # 7 - insercion/es nombre_coleccion /nombre_coleccion_old

    # print("the script has the name %s" % (sys.argv[0]))

    start_time = time.time()
    module = import_module("common_config")
    num_arguments = len(sys.argv)
    mongolo = MongoVersionController(**{'connection_type': 'atlas'})


    if num_arguments == 1: # iniciado desde cron, no hay argumentos de entrada
        mongolo = MongoVersionController(**{'connection_type': 'local'})
        # mongo_client = MongoAireGas(**{'connection_type': 'atlas'})

        if mongolo.connect_db():

            for k, v in dict_instances.items():

                url = "{}/{}".format(LOCAL_ENDPOINT_URL, k)
                rest_consumer = AiregasRestConsumer(**{'url': url})
                response = rest_consumer.get_last_modifications_from_api_rest()

                if isinstance(response, list):
                    for elements in response:
                        # instanciacion de la clase
                        instance = v(**{'entity_data': elements})
                        mongolo.instance = instance
                        instance_json = instance.get_json()
                        print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".
                              format(instance.unique, instance.is_temporal_sequence, instance.collection_name,
                                     instance.collection_name_old))
                        print("Entidad:\n {}".format(instance_json))

                        mongolo.set_collection_info()
                        mongolo.insert_or_version()
                else:
                    print("Error al consumir la API de {}".format(k))

    print("--- Ejecucion de la carga masiva %s seconds ---" % (time.time() - start_time))
