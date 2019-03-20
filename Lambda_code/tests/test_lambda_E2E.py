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
    for filename in os.listdir(THIS_FOLDER+'/test_files'):
        bucket.upload_file(os.path.join(THIS_FOLDER+'/test_files',filename),filename)
        time.sleep(1)
        assert len(list(bucket.objects.filter(Prefix=filename[:-3]+'jpg'))) == 1
