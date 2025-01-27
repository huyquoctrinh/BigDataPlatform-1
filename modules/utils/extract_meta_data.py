from modules.data_models import audio_schema
from flask import request

def extract_metadata_from_request(request):
    audio_id = request.form.get('audio_id')
    filename = request.form.get('filename')
    db_rate = request.form.get('db_rate')
    status = request.form.get('status')
    device = request.form.get('device')
    save_url = None
    return audio_schema.AudioMetadata(
        audio_id,
        filename,
        db_rate,
        status,
        device,
        save_url
    )

