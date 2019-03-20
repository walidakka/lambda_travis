import logging, json, boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event,context):
    filename   = event['Records'][0]['s3']['object']['key']
    bucketname = event['Records'][0]['s3']['bucket']['name']
    s3 = boto3.resource('s3')
    if len(filename.split('.')) == 1:
        newfile = filename + '.jpg'
    else:
        newfile = filename[:-len(filename.split('.')[-1])] + 'jpg'
    s3.Object(bucketname,newfile).copy_from(CopySource='{0}/{1}'.format(bucketname,filename))
    s3.Object(bucketname,filename).delete()
    return {"Oldfile" : filename,
            "Newfile" : newfile}
