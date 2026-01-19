import random
from google.cloud import storage

def create_bucket(bucket_name: str, storage_class: str='STANDARD', location: str='us-central1'):

    gs_client = storage.Client()
    bucket = gs_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    
    gs_client.create_bucket(
        bucket, 
        location=location
    )
    
    print(f"Bucket {bucket.name} creado exitosamente.")
    
    return bucket