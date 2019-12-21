# -*- coding: utf-8 -*-
import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# logger stuff
LOGGER_NAME = "AWS_Batch_Processing"
LOG_FILE = os.path.join(ROOT_DIR, "logger{}{}".format(os.path.sep, LOGGER_NAME))
# json bancos
JSON_SAMPLES = os.path.join(ROOT_DIR, 'json_airegas')
# URL_BASE = "https://swapi.co/api/people"
URL_BASE = "https://swapi.co/api/"

# JSON SAMPLE FILES
CALENDARIO_SAMPLE = os.path.join(JSON_SAMPLES, 'CalendarioEjemploV0.1.json')
PRECIO_FORMULA_SAMPLE = os.path.join(JSON_SAMPLES, 'PrecioFormulaEjemploV0.1.json')
TASA_MOLECULA_SAMPLE = os.path.join(JSON_SAMPLES, 'TasaMoleculaEjemploV0.1.json')
NONINATION_SAMPLE = os.path.join(JSON_SAMPLES, 'NominacionEjemploV0.1.json')
PREVISION_SAMPLE = os.path.join(JSON_SAMPLES, 'PrevisionEjemploV0.1.json')
CALENDARIO_B70_SAMPLE = os.path.join(JSON_SAMPLES, 'CalendarioB70EjemploV0.1.json')
PRECIOS_REGULADOS_SAMPLE = os.path.join(JSON_SAMPLES, 'PreciosReguladosEjemploV0.1.json')
CONSUMO_NOCTURNO_SAMPLE = os.path.join(JSON_SAMPLES, 'ConsumoNocturnoEjemploV0.1.json')
CONSUMO_SAMPLE = os.path.join(JSON_SAMPLES, 'ConsumoEjemploV0.1.json')
DATOS_CLI_SAMPLE = os.path.join(JSON_SAMPLES, 'DatosCLIEjemploV0.1.json')

# FIELDS to check data integrity
# nombre_clase_FIELDS (se invoca por instrospeccion)

# Calendar
Calendar_FIELDS = ['_id', 'ts', 'calendarCode', 'Periods']
Periods_FIELDS = ['idPeriod', 'from', 'to', 'calendarDates', 'active']

# Precio formula
PrecioFormula_FIELDS = ['_id', 'ts', 'formulaCode', 'formulaDes', 'from', 'to', 'compoundIndex', 'prices']
Prices_FIELDS = ["formulaDates", "formulaPrice", "formulaPriceDetail"]

# Tasa_Molecula
Tasa_Molecula_FIELDS = ['_id', 'ts', 'taxCode', 'taxDes', 'from', 'to', 'taxVal']

# Nomination
Nomination_FIELDS = ['_id', 'ts', 'CLI', 'nomination']
Nomination_Details_FIELDS = ['nominationDates', 'nominationVal']

# Prevision
Prevision_FIELDS = ['_id', 'ts', 'CLI', 'prevision']
Prevision_Details_FIELDS = ['forecastDates', 'forecastPrice']

# Calendario_B70
CalendarB70_FIELDS = ['_id', 'ts', 'CLI', 'from', 'to']

# Precios_regulados
Precios_Regulados_FIELDS = ['_id', 'ts', 'regulatedPriceName', 'regulatedDates', 'regulatedVal']

# Consumo_Nocturno
Consumo_Nocturno_FIELDS = ['_id', 'ts', 'CLI', 'dates', 'origin', 'qd']

# Consumo
Consumo_FIELDS = ['_id', 'ts', 'CLI', 'dates', 'origin', 'qd', 'qdElec', 'qdTerm', 'qdRed', 'qdSupRed']

# Datos_CLI
DatosCLI_FIELDS = ['_id', 'ts', 'StartDate', 'EndDate']
Invoice_FIELDS = ['email', 'name', 'IBAN', 'swift', 'paymentTerm', 'paymentMethod']
Supply_FIELDS = ['CUPS', 'address', 'locality', 'postalCode', 'position']
Contract_FIELDS = ['CounterPartyName', 'CounterPartyDocNumber', 'clientName', 'connectionPoint', 'startDate', 'active',
                   'portfolio', 'broker', 'commission']



ENDPOINT_URL = 'https://swapi.co/api/'
