import boto3
import botocore
import os

# Create an S3 client
s3 = boto3.client('s3',
    use_ssl=False,
    endpoint_url='http://%s:9000' % (os.environ['MINIO_IP']), aws_access_key_id='G4FTBCO37J96UCHCQ6DP',
    aws_secret_access_key='dfkViHQM8LLjt54XBuLzhrQtCne8OX5hEhBKMn34')

bucket_name = 'images'

try:
    s3.head_bucket(Bucket=bucket_name)
except botocore.exceptions.ClientError:
    s3.create_bucket(Bucket=bucket_name)

def upload_image(f, object_name):
    s3.upload_fileobj(f, bucket_name, object_name)

def get_image(object_name):
    return s3.get_object(Bucket=bucket_name, Key=object_name)
