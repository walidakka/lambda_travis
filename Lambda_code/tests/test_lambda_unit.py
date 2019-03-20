import boto3, pytest, os, json
from .. import main
from moto import mock_s3

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(THIS_FOLDER, 'event.json')) as f:
    event = json.load(f)
@mock_s3
def test_handler_rename():
    conn = boto3.resource('s3')
    bucket = conn.create_bucket(Bucket=event['Records'][0]['s3']['bucket']['name'])
    bucket.put_object(Key=event['Records'][0]['s3']['object']['key'])
    result = main.handler(event,None)
    assert len(list(bucket.objects.filter(Prefix=result['Newfile']))) == 1
    assert len(list(bucket.objects.filter(Prefix=result['Oldfile']))) == 0
