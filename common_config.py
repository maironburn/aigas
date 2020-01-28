# -*- coding: utf-8 -*-
import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# logger stuff
LOGGER_NAME = "AWS_Batch_Processing"
LOG_FILE = os.path.join(ROOT_DIR, "logger{}{}".format(os.path.sep, LOGGER_NAME))
URL_BASE = "https://swapi.co/api/"

# JSON SAMPLE FILES
JSON_SAMPLES = os.path.join(ROOT_DIR, 'json_airegas')
CALENDAR_SAMPLE = os.path.join(JSON_SAMPLES, 'CalendarioEjemploV0.1.json')
FORMULA_PRICE_SAMPLE = os.path.join(JSON_SAMPLES, 'PrecioFormulaEjemploV0.1.json')
MOLECULE_TAX_SAMPLE = os.path.join(JSON_SAMPLES, 'TasaMoleculaEjemploV0.1.json')
NOMINATION_SAMPLE = os.path.join(JSON_SAMPLES, 'NominacionEjemploV0.1.json')
FORECAST_SAMPLE = os.path.join(JSON_SAMPLES, 'PrevisionEjemploV0.1.json')
B70_CALENDAR_SAMPLE = os.path.join(JSON_SAMPLES, 'CalendarioB70EjemploV0.1.json')
REGULATED_PRICE_SAMPLE = os.path.join(JSON_SAMPLES, 'PreciosReguladosEjemploV0.1.json')
NIGHT_CONSUMPTION_SAMPLE = os.path.join(JSON_SAMPLES, 'ConsumoNocturnoEjemploV0.1.json')
CONSUMPTION_SAMPLE = os.path.join(JSON_SAMPLES, 'ConsumoEjemploV0.1.json')
CLI_SAMPLE = os.path.join(JSON_SAMPLES, 'DatosCLIEjemploV0.1.json')
GAS_QUALITY_DETAIL_SAMPLE = os.path.join(JSON_SAMPLES, 'DetallesCalidadGasEjemploV0.1.json')
ATR_AMOUNT_SAMPLE = os.path.join(JSON_SAMPLES, 'ImportesATRPassthroughEjemploV0.1.json')

# test para AWS Gateway


TRACKER_SAMPLES = os.path.join(ROOT_DIR, 'json_tracker')
ATR_DISTRIBUTION_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-ATRDistribucion-EjemploV1.0.json')
ATR_UPSTREAM_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-ATRUpstream-EjemploV1.0.json')
BLOQUE_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-BloqueFirme-EjemploV1.0.json')
BONIFICACION_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-BonificacionNominacion-EjemploV1.0.json')
COBERTURA_SWAP_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-CoberturaSWAP-EjemploV1.0.json')
COSTES_TASAS_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-CostesTasas-EjamploV1.0.json')
IMPORTE_FIJO_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-ImporteFijo-EjemploV1.0.json')
SERVICIO_MOLECULA_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-ServicioMolecula-EjemploV1.0.json')
TASA_USO_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-TasaUso-EjemploV1.0.json')
TOLERANCIA_SAMPLE = os.path.join(TRACKER_SAMPLES, 'Tracker-Tolerancia-EjemploV1.0.json')

# FIELDS to check data integrity
# nombre_clase_FIELDS (se invocan por instrospeccion)

# Calendar
Calendario_FIELDS = ['calendar_code', 'Expiration_Date', 'list_periods']
Periods_FIELDS = ['id_period', 'from', 'to', 'calendar_dates', 'active']

# Nomination
Nominacion_FIELDS = ['CLI', 'nomination']
Nomination_Details_FIELDS = ['calendar_dates', 'nominationVal']

# Tasa_Molecula
TasaMolecula_FIELDS = ['taxCode', 'taxDes', 'from', 'to', 'taxVal']

# Precio formula
PrecioFormula_FIELDS = ['formulaCode', 'formulaDes', 'from', 'to', 'compoundIndex', 'prices']
Prices_FIELDS = ["formulaDates", "formulaPrice", "formulaPriceDetail"]

# Prevision
Forecast_FIELDS = ['CLI', 'forecast']
Forecast_Details_FIELDS = ['forecastDates', 'forecastPrice']

# Calendario_B70
B70_Calendar_FIELDS = ['CLI', 'from', 'to']

# Precios_regulados
Regulated_Price_FIELDS = ['regulatedPriceName', 'regulatedDates', 'regulatedVal']

# Consumo_Nocturno
Night_Consumption_FIELDS = ['CLI', 'dates', 'origin', 'qd']

# Consumo
Consumption_FIELDS = ['CLI', 'dates', 'origin', 'qd', 'qdElec', 'qdTerm', 'qdRed', 'qdSupRed']

# Datos_CLI
Cli_FIELDS = ['StartDate', 'EndDate']
Invoice_FIELDS = ['email', 'name', 'IBAN', 'swift', 'paymentTerm', 'paymentMethod']
Supply_FIELDS = ['CUPS', 'address', 'locality', 'postalCode', 'position']
Contract_FIELDS = ['CounterPartyName', 'CounterPartyDocNumber', 'clientName', 'connectionPoint', 'startDate', 'active',
                   'portfolio', 'broker', 'commission']

# Detalle calidad de gas
Gas_Quality_Detail_FIELDS = ['CLI', 'date', 'meter', 'detailPCS', 'detailPCI', 'detailDensity', 'detailN2',
                             'detailPressure', 'detailTemp', 'detailValueZ', 'detailValueK', 'detailLectm3',
                             'detailConsm3',
                             'detailAdjustementskWh', 'detailConskWh', 'detailCO2'
                             ]

# Importes ATR
Atr_Amount_FIELDS = ['CLI', 'From', 'To', 'ATRPrices']
ATRPrices_FIELDS = ['TPAId', 'TPAConcept', 'TPAConceptAmount']

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
# ENDPOINT_URL = 'https://swapi.co/api/'

ENDPOINT_URL = 'http://airegastestapp1.axpohosting.local:8081/'
LOCAL_ENDPOINT_URL = 'http://127.0.0.1:8080/'
# CALENDARIO_ENDPOINT = 'http://airegastestapp1.axpohosting.local:8081/Calendario?from=2020-01-01'
