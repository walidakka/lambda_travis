import boto3
from .. import main
from moto import mock_s3
import pytest


event = {}

with open()

@mock_s3
def test_handler():
    conn = boto3.resource('s3', region_name='eu-west-1')
    bucket = conn.create_bucket(Bucket=event['Records'][0]['s3']['bucket']['name'])
    bucket.put_object(Key=event['Records'][0]['s3']['object']['key'])
    result = main.handler(event,None)
    assert len(list(bucket.objects.filter(Prefix=result['body']['Newfile']))) == 1
    assert len(list(bucket.objects.filter(Prefix=result['body']['Oldfile']))) == 0
