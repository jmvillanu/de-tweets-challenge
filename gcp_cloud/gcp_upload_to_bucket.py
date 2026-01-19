from google.cloud import storage
from pathlib import Path

def upload_to_bucket(bucket_name: str, source_file: Path, target_file_name: str):
    gs_client = storage.Client()

    bucket = gs_client.bucket(bucket_name)
    blob = bucket.blob(target_file_name)

    blob.upload_from_filename(source_file)

    return f"Archivo {target_file_name} subido a {bucket_name} satisfactoriamente"