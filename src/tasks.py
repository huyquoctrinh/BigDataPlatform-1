import os
from celery import Celery
# from workers.update_metadata import update_metadata
# from workers.upload_file import upload_file_to_minio
import logging
from boto3 import client
import dotenv
import ast 
# from workers.db_handler import AtlasClient
from publisher.kafka_producer import Producer
import json

dotenv.load_dotenv()

logger = logging.getLogger(__name__)

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.update_metadata')
def update_metadata_task(results_dict):
    logger.info(f"Updating metadata for {results_dict['audio_id']}")
    return 1

@celery.task(name='tasks.ingest_data')
def ingest_data_task(
    metadata_dict: dict
):
    logger.log(logging.INFO, f"Inserting new metadata for {metadata_dict['audio_id']}")
    data_publisher = Producer(topic='test')
    data_publisher.send(json.dumps(metadata_dict).encode('utf-8'))
    return metadata_dict

@celery.task(name='tasks.upload_file_to_minio')
def upload_file_to_minio_task(
    key: str
):
    s3_client = client(
        "s3",
        endpoint_url= os.environ.get("MINIO_ENDPOINT"),
        aws_access_key_id=os.environ.get("MINIO_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("MINIO_SECRET_KEY"),
        use_ssl=False,
    )
    # try:
    logger.info(f"Update data key: {key}")
    basename = key.split("/")[-1]
    s3_client.upload_file(
        key,
        "mimic-data",
        basename
    )
    return True
    # except Exception as e:
        # return False
