# -*- coding: utf-8 -*-
import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# logger stuff
LOGGER_NAME = "AWS_Batch_Processing"
LOG_FILE = os.path.join(ROOT_DIR, "logger{}{}".format(os.path.sep, LOGGER_NAME))


DATA_LOCAL = {'db_name': "airegas",
              'host': 'localhost',
              'port': "27017",
              'user': '',
              'pwd': ''
              }

ATLAS_DATA = {'db_name': "db_test",
              'host': 'liqgas-develop-nfezk.mongodb.net',
              'port': "27017",
              'user': '',
              'pwd': ''
              }

collection_mapper = {
    'Calendario': 'Calendar',
    'Nominacion': 'Nomination',
    'TasaMolecula': 'Molecule_Tax',
    'PrecioFormula': 'Formula_Price'
}

MONGODB_LOCAL = "mongodb://{}:{}".format(DATA_LOCAL['host'], DATA_LOCAL['port'], DATA_LOCAL['db_name'])
MONGODB_ATLAS = "mongodb+srv://{}:{}@{}".format(ATLAS_DATA['user'], ATLAS_DATA['pwd'], ATLAS_DATA['host'],
                                                ATLAS_DATA['db_name'])

XLXS_CARGA_MASIVA = os.path.join(os.path.join(ROOT_DIR, 'plantilla_carga_masiva'), 'PlantillaLanzamientoManual.xlsx')

# URL API REST
ENDPOINT_URL = 'http://airegastestapp1.axpohosting.local:8081/'
LOCAL_ENDPOINT_URL = 'http://127.0.0.1:8080/'
