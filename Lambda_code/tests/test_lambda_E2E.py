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
    bucket = s3.Bucket(str(output['bucket_name']['value']))
    #bucket.put_object(Key="something.ezazekssea.zeaaze.sss",Body=b'foobar')
    bucket.upload_file(THIS_FOLDER+'test_files/1280px-Git-logo.svg.png')
    time.sleep(3)
    assert len(list(bucket.objects.filter(Prefix="1280px-Git-logo.svg.jpg"))) == 1
    assert len(list(bucket.objects.filter(Prefix="1280px-Git-logo.svg.png"))) == 0
