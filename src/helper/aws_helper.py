from botocore.client import ClientError
import boto3
import logging
import botocore
from botocore.client import ClientError
import json
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_credentials():
    aws_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')

    client = boto3.client(
        's3',
        # Hard coded strings as credentials, not recommended.
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret
    )

    return client


def check_bucket_exists(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False

    return exists


def write_to_s3(**kwargs):
    logger.info("write_to_s3 -> bucket:  {}, file: {}".format(kwargs['bucket_name'], kwargs['path_and_name_with_ext']))
    client = boto3.client('s3')
    client.put_object(Body=kwargs['data'], Bucket=kwargs['bucket_name'], Key=kwargs['path_and_name_with_ext'])
    logger.info("fichero json creado con exito: {}".format(kwargs['path_and_name_with_ext']))


def read_s3_bucket(bucket, item):
    try:
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, item)
        response = obj.get()['Body'].read().decode('utf-8')
        print("response: {}".format(type(response)))
        return json.loads(response)

        # return response
    except ClientError as ex:
        if ex.response['Error']['Code'] == 'NoSuchKey':
            logger.info('No object found - returning empty')

    except Exception as e:
        logger.info('No object found - returning empty {}'.format(e))

    return None
