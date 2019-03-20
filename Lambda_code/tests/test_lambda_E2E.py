import boto3
import pytest
import os, time
import json
from .. import main

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(THIS_FOLDER, 'output.json')) as f:
    output = json.load(f)

def test_lambda_E2E():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(output['bucket_name']['value'])
    object = s3.Object(output['bucket_name'],"something.ezazekssea.zeaaze.sss")
    time.sleep(3)
    assert len(list(bucket.objects.filter(Prefix="something.ezazekssea.zeaaze.jpg"))) == 1
    assert len(list(bucket.objects.filter(Prefix="something.ezazekssea.zeaaze.sss"))) == 0
