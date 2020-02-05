from src.helper.common_helper import get_entity_from_samples
from src.mongodb.mongo_client import MongoAireGas
from common_config import *
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
from src.model.forecast.prevision import Prevision
from src.model.regulated_price.regulated_price import RegulatedPrice
from src.model.molecule_tax.molecule_tax import TasaMolecula
from src.helper.airegasrestconsumer import AiregasRestConsumer
from src.controller.mongo_contoller import MongoVersionController
import time
import sys
import logging
import boto3
import os
from src.helper.aws_helper import *
from src.controller.batch_controller import BatchController

dict_instances_mapper = {
    'Calendario': Calendario,
    'Nominacion': Nominacion,
    'Prevision': Prevision,
    'PrecioFormula': PrecioFormula
    # 'B70_Calendar': B70_Calendar,
    # 'Atr_Amount': Atr_Amount,
    # 'Consumption': Consumption,
    # 'Night_Consumption': Night_Consumption,
    # 'Cli': Cli,
    # 'Gas_Quality_Detail': Gas_Quality_Detail,

    # 'Formula_Price': PrecioFormula,

    # 'Regulated_Price': Regulated_Price,
    # 'TasaMolecula': TasaMolecula
}


def check_collection(collecion_to_ingest):
    # comprobacion de q el argumento es valido
    if collecion_to_ingest in dict_instances_mapper.keys():
        # clase asociada en dict
        return dict_instances_mapper[collecion_to_ingest]

    print("Argumento/Coleccion no valida: {}".format(collecion_to_ingest))
    return None


BUCKET_NAME = os.getenv('BUCKET_NAME') or 'liqgas-des'
FILE = os.getenv('KEY') or 'airegas_carga_masiva_batch.json'
DOCUMENTDB_URL = os.getenv('DOCUMENTDB_URL')
DATABASE = os.getenv('DATABASE')
AIREGAS_ENDPOINT_URL = os.getenv('AIREGAS_ENDPOINT_URL') or 'http://127.0.0.1:8080/'

if __name__ == '__main__':

    start_time = time.time()
    module = import_module("common_config")
    num_arguments = len(sys.argv)

    if num_arguments == 2 and set_credentials():
        instance = check_collection(sys.argv[1])
        mongo_ver_controller = MongoVersionController(**{'DOCUMENTDB_URL': DOCUMENTDB_URL, 'DATABASE': DATABASE})
        if instance and mongo_ver_controller.connect_db():

            batch_controller = BatchController(
                **{'bucket': BUCKET_NAME, 'key': FILE, 'instance': instance,
                   'mongo_version_controller': mongo_ver_controller,
                   'AIREGAS_ENDPOINT_URL': AIREGAS_ENDPOINT_URL})
            # se comprueba si existe en S3 el ficero json de carga masiva
            if batch_controller.check_if_carga_masiva():
                batch_controller.do_massive_procedure()

            else:
                print("Modo Delta")
                batch_controller.do_delta_procedure()
        else:
            print("Argumento invalido o Sin conexion a la base de datos, URL: {}, Database: {}".format(DOCUMENTDB_URL,
                                                                                                       DATABASE))
    else:
        print("Batch no pudo iniciarse, numero de Argumentos invalido: {}".format(sys.argv[1]))

    print("--- Ejecucion de la carga masiva %s seconds ---" % (time.time() - start_time))
