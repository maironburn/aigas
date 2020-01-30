from botocore.client import ClientError
import boto3


def check_bucket_resource(bucket):
    try:
        s3 = boto3.resource('s3')
        s3.meta.client.head_bucket(Bucket=bucket.name)

        return True

    except ClientError:
        print("Bucket: {} not found".format(bucket))
        # The bucket does not exist or you have no access.

    return False


def read_s3_bucket(bucket, item):

    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, item)
    body = obj.get()['Body'].read()
