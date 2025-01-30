import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def update_file(
    bucket_name: str,
    file_name: str,
    file_path: str,
    s3_client: boto3.client
):
    s3_client.upload_file(
        file_path,
        bucket_name,
        file_name
    )
    return True

s3_client = boto3.client(
    "s3",
    endpoint_url= os.environ.get("MINIO_ENDPOINT"),
    aws_access_key_id=os.environ.get("MINIO_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("MINIO_SECRET_KEY"),
    use_ssl=False,
)

update_file(
    "mimic-data",
    "test.txt",
    "test.txt",
    s3_client
)


# list_buckets = s3_client.list_buckets()
# print(list_buckets)