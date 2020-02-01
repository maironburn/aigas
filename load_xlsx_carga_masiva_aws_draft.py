import pandas as pd
import json
import boto3
import logging
import uuid
from urllib.parse import unquote_plus
# from src.helper.aws_helper import write_to_s3
import os
from aws_logging_handlers.S3 import S3Handler

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

bucket_key = os.getenv('BUCKET_KEY_MASSIVE')
bucket_key_cli = os.getenv('BUCKET_KEY_CLI')
log_bucket = os.getenv('LOG_BUCKET_NAME')


def get_aws_logger(log_file_name):

    s3_handler = S3Handler(log_file_name, log_bucket)
    formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d} %(levelname)s - %(message)s')
    s3_handler.setFormatter(formatter)
    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)
    logger.addHandler(s3_handler)

    return logger

pandas_row_mapper = {0: 'TasaMoleAcula', 1: 'PrecioFormula', 2: 'Calendario', 3: 'Prevision',
                     4: 'Nominacion', 5: 'precio', 6: 'CLI', 7: 'Consumo', 8: 'Calidad_gas', 9: 'calendariob70',
                     10: 'importeAtr', 11: 'Coeficiente', 12: 'idContract'}

logger= get_aws_logger("test_aws_log")


def write_to_s3(**kwargs):
    logger.info("write_to_s3 -> bucket:  {}, file: {}".format(kwargs['bucket_name'], kwargs['key']))
    client = boto3.client('s3')
    client.put_object(Body=kwargs['data'], Bucket=kwargs['bucket_name'], Key=kwargs['key'])
    logger.info("fichero json creado con exito: {}".format(kwargs['key']))


def do_pandas_job(download_path):
    df = pd.read_excel(download_path)
    logger.info("EXCEL leido de {}".format(download_path))
    df = df.loc[:12, 'colecciones':'ListCode'].astype('str')  # filtro columnas
    logger.info("EXCEL sliced")
    df = df.rename(index=pandas_row_mapper)
    logger.info("Renombrado de rows")
    df = df.loc[:, 'From':'ListCode'].replace('nan', '', regex=True)
    json_massive_load = json.loads(df.T.to_json())
    logger.info("Df transpose")
    logger.info("generado json para la ingesta: \n{}".format(json_massive_load))

    return json_massive_load


def lambda_handler(event, context):
    logger.info("lambda para la carga masiva instanciada")
    s3_client = boto3.client('s3')

    for record in event['Records']:
        logger.info("Disparado evento ObjectCreated")
        logger.info("EVENT")
        logger.info(event)

        bucket = record['s3']['bucket']['name']

        logger.info("bucket: {}".format(bucket))
        key = unquote_plus(record['s3']['object']['key'])
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

        logger.info("fichero descargado en: download_path-> {} ".format(download_path))
        s3_client.download_file(bucket, key, download_path)
        logger.info("downloadedd file ")

        json_massive_load = do_pandas_job(download_path)

        kw = {'data': json.dumps(json_massive_load), 'bucket_name': bucket,
              'key': bucket_key}

        write_to_s3(**kw)

    logging.shutdown()