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
import logging
import boto3
import os
from src.helper.aws_helper import *
from src.controller.batch_controller import BatchController


dict_instances_mapper = {'Calendario': Calendario
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
                         # 'TasaMolecula': TasaMolecula
                         }

# mapea las clases con sus colecciones en MongoDB para la persistencia
'''

si no llegan argumentos
los respectivos .py del batch (q conforman el proceso de cada coleccion) consultan en DocumentDB por la fecha max lastmodified...
-> consume la api informando este param en la query, se trae los datos y los persiste en DocumentDB según su lógica de versionado


Logica de la carga masiva / delta

si existe el fichero json de la carga masiva
Las colecciones que esten informadas consumiran la API a partir de esos datos

Las colecciones no informadas procederan a la mecanica  delta
-el batch consulta en DocumentDB por la fecha max lastmodified...
-consume la api informando este param en la query, se trae los datos y los persiste en DocumentDB según su lógica de versionado


FINALLY:
    persistencia en DocumentDB


'''

''''
Comprobamos si el fichero carga masiva existe en el bucket

'''

BUCKET_NAME = os.getenv('BUCKET_NAME') or 'liqgas-des'
FILE = os.getenv('BUCKET_NAME') or 'airegas_carga_masiva_batch.json'
DOCUMENTDB_URL= os.getenv('DOCUMENTDB_URL')
DATABASE= os.getenv('DATABASE')

if __name__ == '__main__':

    start_time = time.time()
    module = import_module("common_config")
    num_arguments = len(sys.argv)

    if num_arguments == 2 and set_credentials():
        collecion_to_ingest = sys.argv[1]

        #comprobacion de q el argumento es valido
        if collecion_to_ingest in dict_instances_mapper.keys():
            # clase asociada en dict
            instance = dict_instances_mapper[collecion_to_ingest]
            batch_controller = BatchController(**{'bucket': BUCKET_NAME, 'key': FILE, 'collection': instance})

            mongolo = MongoVersionController(**{'DOCUMENTDB_URL': DOCUMENTDB_URL, 'DATABASE': DATABASE})
            if mongolo.connect_db():
                # se comprueba si existe en S3 el ficero json de carga masiva
                if batch_controller.check_if_carga_masiva():
                    # se procesan los datos del json de carga masiva relativos a la colleccion que entra como argumento
                    data_to_build_query = batch_controller.process_data_carga_masiva()
                    url = "{}/{}".format(LOCAL_ENDPOINT_URL, instance.__name__)
                    # construccion de la query para consumir de AireGas
                    rest_consumer = AiregasRestConsumer(**{'url': url})
                    response = rest_consumer.query_for_api_rest(**data_to_build_query)
                    if isinstance(response, list):
                        # insercion de DocumentDB de la coleccion recuperada del API
                        for elements in response:
                            collection_entity = instance(**{'entity_data': elements})
                            mongolo.instance = collection_entity
                            instance_json = collection_entity.get_json()
                            inserted_id=mongolo.insert_or_version()
                            print("Insercion en Document DB, coleccion: {} , id: {}".format(instance.__name__, inserted_id))
                    else:
                        print("Sin acesso a  la API, url : {}".format(url))
                else:
                    print ("Modo Delta")

            else:
                print ("Sin conexion a la base de datos, URL: {}, Database: {}".format(DOCUMENTDB_URL, DATABASE))
                # consulta por lastModified
                # consume APi
                # persiste
                pass

        else:
            print("Batch no pudo iniciarse, Argumento no reconocido: {}".format(sys.argv[1]))
    #
    #
    #
    #         # si existe el fichero de carga masiva en bucket
    #         #   #si: leer fichero
    #         #   #no: delta
    #
    #         mongolo = MongoVersionController(**{'connection_type': 'local'})
    #         # mongo_client = MongoAireGas(**{'connection_type': 'atlas'})
    #
    #         if mongolo.connect_db():
    #
    #             for k, v in dict_instances_mapper.items():
    #
    #                 url = "{}/{}".format(LOCAL_ENDPOINT_URL, k)
    #                 rest_consumer = AiregasRestConsumer(**{'url': url})
    #                 response = rest_consumer.get_last_modifications_from_api_rest()
    #
    #                 if isinstance(response, list):
    #                     for elements in response:
    #                         # instanciacion de la clase
    #                         instance = v(**{'entity_data': elements})
    #                         mongolo.instance = instance
    #                         instance_json = instance.get_json()
    #                         print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".
    #                               format(instance.unique, instance.is_temporal_sequence, instance.collection_name,
    #                                      instance.collection_name_old))
    #                         print("Entidad:\n {}".format(instance_json))
    #
    #                         mongolo.set_collection_info()
    #                         mongolo.insert_or_version()
    #                 else:
    #                     print("Error al consumir la API de {}".format(k))
    #
    # print("--- Ejecucion de la carga masiva %s seconds ---" % (time.time() - start_time))
