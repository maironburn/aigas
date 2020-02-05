import pandas as pd
import json
import boto3
import logging
import uuid
from urllib.parse import unquote_plus
import os
from aws_logging_handlers.S3 import S3Handler

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


logger = get_aws_logger("lambda_Batch_inicio_manual")


def write_to_s3(**kwargs):
    logger.info("write_to_s3 -> bucket:  {}, file: {}".format(kwargs['bucket_name'], kwargs['key']))
    client = boto3.client('s3')
    client.put_object(Body=kwargs['data'], Bucket=kwargs['bucket_name'], Key=kwargs['key'])
    logger.info("fichero json creado con exito: {}".format(kwargs['key']))


def do_pandas_job(download_path):
    try:

        pandas_row_mapper = {0: 'TasaMolecula', 1: 'PrecioFormula', 2: 'Calendario', 3: 'Prevision',
                             4: 'Nominacion', 5: 'precio', 6: 'CLI', 7: 'Consumo', 8: 'Calidad_gas', 9: 'calendariob70',
                             10: 'importeAtr', 11: 'Coeficiente', 12: 'idContract'}

        df = pd.read_excel(download_path)
        logger.info("EXCEL leido de {}".format(download_path))
        # filtro columnas
        df = df.loc[:12, 'colecciones':'ListCode'].astype('str')
        logger.info("EXCEL sliced")
        df = df.rename(index=pandas_row_mapper)
        logger.info("Renombrado de rows")
        df = df.loc[:, 'From':'ListCode'].replace('nan', '', regex=True)
        json_massive_load = json.loads(df.T.to_json())
        logger.info("Df transpose")
        logger.info("generado json para la ingesta: \n{}".format(json_massive_load))
        json_id_contract = None

        if 'idContract' in json_massive_load.keys() and len(json_massive_load['idContract']['From'].split(',')):
            json_id_contract = json_massive_load['idContract']['From'].split(',')
            logger.info("json idContract: {}".format(json_id_contract))

        return json_massive_load, json_id_contract

    except Exception as e:
        logger.error("Error en la lectura Pandas: {}".format(e))

    return None


def send_job_to_batch():
    client = boto3.client('batch')

    logger.info("lambda_invoke_batch")
    trabajos = ['job_calendar', 'job_nomination']
    job_queue = 'test_batch_queue_V1'

    try:

        for j in trabajos:
            client.submit_job(
                jobName=j,
                jobQueue=job_queue,
                jobDefinition='calendario:1'
            )
            logger.info("trabajo :{}, enviado a la cola: {}".format(j, job_queue))
        return True
    except Exception as e:
        logger.error("Error al despachar los trabajos al Batch: {}".format(e))

    return False


def lambda_handler(event, context):
    logger.info("lambda para la carga masiva instanciada")
    s3_client = boto3.client('s3')

    for record in event['Records']:
        logger.info("Disparado evento ObjectCreated")
        logger.info("EVENT_INFO: {} ".format(event))

        bucket = record['s3']['bucket']['name']

        logger.info("bucket: {}".format(bucket))
        key = unquote_plus(record['s3']['object']['key'])
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

        logger.info("fichero descargado en: download_path-> {} ".format(download_path))
        s3_client.download_file(bucket, key, download_path)
        logger.info("downloadedd file ")

        json_massive_load, json_id_contract = do_pandas_job(download_path)
        if json_massive_load:
            kw = {'data': json.dumps(json_massive_load), 'bucket_name': bucket,
                  'key': bucket_key}

            write_to_s3(**kw)

            if json_id_contract:
                logger.info("pandas_before save->type:{} -> {}".format(type(json_id_contract), json_id_contract))
                kw = {'data': json.dumps({'idContract': json_id_contract}), 'bucket_name': bucket,
                      'key': bucket_key_cli}
                write_to_s3(**kw)

            '''
            if  not send_job_to_batch():
                logger.error("Error al enviar los trabajos a Batch")
            '''
        else:
            logger.error("No se pudo completar el proceso, fichero corrupto: {}".format(key))

    logging.shutdown()
