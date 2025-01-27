from flask import request, jsonify
import boto3
from celery import shared_task

@shared_task(ignore_result=False)
def upload_file_to_minio(
    s3_client,
    bucket_name,
    key
):
    try:
        s3_client.upload_file(
            key,
            bucket_name,
            key
        )
        return True
    except Exception as e:
        return False