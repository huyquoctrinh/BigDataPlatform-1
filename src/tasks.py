import os
from celery import Celery
from workers.update_metadata import update_metadata
import logging
from boto3 import client
import dotenv

dotenv.load_dotenv()

logging.basicConfig(filename="./worker_logs/worker.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.update_metadata')
def update_metadata_task(results_dict):
    logging.info(f"Updating metadata for {results_dict['audio_id']}")
    return 1

@celery.task(name='tasks.upload_file_to_minio')
def upload_file_to_minio(
    key, bucket_name
):
    s3_client = client(
        "s3",
        endpoint_url= os.environ.get("MINIO_ENDPOINT"),
        aws_access_key_id=os.environ.get("MINIO_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("MINIO_SECRET_KEY"),
        use_ssl=False,
    )
    try:
        s3_client.upload_file(
            key,
            bucket_name,
            key
        )
        return True
    except Exception as e:
        return False
