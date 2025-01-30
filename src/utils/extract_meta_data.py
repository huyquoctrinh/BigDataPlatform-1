from data_models import audio_schema

def extract_metadata_from_request(request):
    audio_id = request.form.get('id')
    filename = request.files["audio_file"].filename
    db_rate = request.form.get('db')
    status = request.form.get('status')
    device = request.form.get('device')
    tag = request.form.get('tag')
    save_url = "http://minio:9000/" + tag + "/" + filename.split("/")[-1] 
    return audio_schema.AudioMetadata(
        audio_id,
        filename,
        db_rate,
        status,
        device,
        save_url
    )

