import boto3
from celery import shared_task

def upload_file_to_minio(
    cfg
):
    try:
        s3_client.upload_file(
            cfg['key'],
            cfg['bucket_name'],
            cfg['key'].split("/")[-1],
        )
        return True
    except Exception as e:
        return False