import os
import json
import tempfile
from google.cloud import storage
from q1 import q1

OUTPUT_PREFIX = "outputs/"

def process_tweets_data(event, context):

    bucket_name = event["bucket"]
    blob_name = event["name"]

    if blob_name.startswith(OUTPUT_PREFIX):
        print(f"Skipping output file: {blob_name}")
        return

    print(f"Processing gs://{bucket_name}/{blob_name}")

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        blob.download_to_filename(tmp.name)
        local_input_path = tmp.name

    raw_result = q1(local_input_path)
    
    result = [
        {
            "date": d.isoformat(),
            "username": u
        }
        for d, u in raw_result
    ]


    output_local_path = "/tmp/q1_output.json"
    with open(output_local_path, "w") as f:
        json.dump(result, f)


    output_blob_name = f"{OUTPUT_PREFIX}{os.path.basename(blob_name)}.json"
    output_blob = bucket.blob(output_blob_name)
    output_blob.upload_from_filename(output_local_path)

    print(f"Output written to gs://{bucket_name}/{output_blob_name}")
