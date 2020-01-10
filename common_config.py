# -*- coding: utf-8 -*-
import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# logger stuff
LOGGER_NAME = "AWS_Batch_Processing"
LOG_FILE = os.path.join(ROOT_DIR, "logger{}{}".format(os.path.sep, LOGGER_NAME))

# URL_BASE = "https://swapi.co/api/people"
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

# FIELDS to check data integrity
# nombre_clase_FIELDS (se invocan por instrospeccion)

# Calendar
Calendar_FIELDS = ['_id', 'ts', 'calendarCode', 'Periods']
Periods_FIELDS = ['idPeriod', 'from', 'to', 'calendarDates', 'active']

# Precio formula
Formula_Price_FIELDS = ['_id', 'ts', 'formulaCode', 'formulaDes', 'from', 'to', 'compoundIndex', 'prices']
Prices_FIELDS = ["formulaDates", "formulaPrice", "formulaPriceDetail"]

# Tasa_Molecula
Molecule_Tax_FIELDS = ['_id', 'ts', 'taxCode', 'taxDes', 'from', 'to', 'taxVal']

# Nomination
Nomination_FIELDS = ['_id', 'ts', 'CLI', 'nomination']
Nomination_Details_FIELDS = ['nominationDates', 'nominationVal']

# Prevision
Forecast_FIELDS = ['_id', 'ts', 'CLI', 'forecast']
Forecast_Details_FIELDS = ['forecastDates', 'forecastPrice']

# Calendario_B70
B70_Calendar_FIELDS = ['_id', 'ts', 'CLI', 'from', 'to']

# Precios_regulados
Regulated_Price_FIELDS = ['_id', 'ts', 'regulatedPriceName', 'regulatedDates', 'regulatedVal']

# Consumo_Nocturno
Night_Consumption_FIELDS = ['_id', 'ts', 'CLI', 'dates', 'origin', 'qd']

# Consumo
Consumption_FIELDS = ['_id', 'ts', 'CLI', 'dates', 'origin', 'qd', 'qdElec', 'qdTerm', 'qdRed', 'qdSupRed']

# Datos_CLI
Cli_FIELDS = ['_id', 'ts', 'StartDate', 'EndDate']
Invoice_FIELDS = ['email', 'name', 'IBAN', 'swift', 'paymentTerm', 'paymentMethod']
Supply_FIELDS = ['CUPS', 'address', 'locality', 'postalCode', 'position']
Contract_FIELDS = ['CounterPartyName', 'CounterPartyDocNumber', 'clientName', 'connectionPoint', 'startDate', 'active',
                   'portfolio', 'broker', 'commission']

# Detalle calidad de gas
Gas_Quality_Detail_FIELDS = ['_id', 'ts', 'CLI', 'date', 'meter', 'detailPCS', 'detailPCI', 'detailDensity', 'detailN2',
                             'detailPressure', 'detailTemp', 'detailValueZ', 'detailValueK', 'detailLectm3',
                             'detailConsm3',
                             'detailAdjustementskWh', 'detailConskWh', 'detailCO2'
                             ]

# Importes ATR
Atr_Amount_FIELDS = ['_id', 'ts', 'CLI', 'From', 'To', 'ATRPrices']
ATRPrices_FIELDS = ['TPAId', 'TPAConcept', 'TPAConceptAmount']

MONGODB_TEST = {'db_name': "airegas",
                'host': 'localhost',
                'port': "27017",
                'user': '',
                'pwd': ''
                }

# URL API REST
ENDPOINT_URL = 'https://swapi.co/api/'
