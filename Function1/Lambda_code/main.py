import logging, json, boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#
def handler(event,context):
    filename   = event['Records'][0]['s3']['object']['key']
    bucketname = event['Records'][0]['s3']['bucket']['name']
    s3 = boto3.resource('s3')
    newfile = filename[:-3]+'jpg'
    s3.Object(bucketname,newfile).copy_from(CopySource='{0}/{1}'.format(bucketname,filename))
    s3.Object(bucketname,filename).delete()
    return {
        "statusCode": 200,
        "body": {"Oldfile" : filename,
                 "Newfile" : newfile
        }
    }
