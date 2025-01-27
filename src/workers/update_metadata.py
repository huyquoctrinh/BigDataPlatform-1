from utils.extract_meta_data import extract_metadata_from_request
import logging

def update_metadata(metadata_dict):
    logging.info(f"Updating metadata for {metadata_dict['audio_id']}")
    return True