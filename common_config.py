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

# FIELDS to check data integrity
CALENDARIO_FIELDS = ['_id', 'ts', 'calendarCode', 'Periods']
PERIODS_FIELDS = ['idPeriod', 'from', 'to', 'calendarDates', 'active']


ENDPOINT_URL='https://swapi.co/api/'