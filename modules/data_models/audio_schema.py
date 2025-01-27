class AudioMetadata:
    def __init__(
        self,
        audio_id,
        filename,
        db_rate,
        status,
        device,
        save_url = None
    ):
        self.audio_id = audio_id
        self.filename = filename
        self.status = status
        self.device = device
        self.db_rate = db_rate
        if save_url==None:
            self.save_url = ""
    def to_dict(self):
        return {
            'audio_id': self.audio_id,
            'filename': self.filename,
            'save_url': self.save_url
            'db_rate': self.db_rate,
            'status': self.status,
            'device': self.device,
        }
    