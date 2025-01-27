from celery import shared_task
from modules.utils.extract_data import extract_metadata_from_request

@shared_task(ignore_result=False)
def extract_metadata(request):
    metadata = extract_metadata_from_request(request)
    return metadata
