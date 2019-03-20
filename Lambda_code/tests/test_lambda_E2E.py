import boto3
import pytest
import os, time
import json
from ..Lambda_code import main

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(THIS_FOLDER, 'output.json')) as f:
    output = json.load(f)

def test_lambda_E2E():
    s3 = boto3.resource('s3', region_name='eu-west-1')
    object = s3.Object(output['bucket_name'],"something.ezazekssea.zeaaze.sss")
    time.sleep(3)
    assert object.key == "something.ezazekssea.zeaaze.jpg"
