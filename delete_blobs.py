import os
import time
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def delete_blobs(num_of_files=10000):
    """Delete the previously uploaded blobs"""

    load_dotenv()

    connect_str = os.getenv('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = os.getenv('AZURE_BLOB_STORAGE_CONTAINER_NAME')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    start = time.time()
    for i in range(num_of_files):
        container_client.delete_blob(blob=f'testing/{i}_dummy_file.txt', delete_snapshots="include")
    end = time.time()
    print(f"Deleted {num_of_files} files in {end - start} secs")

delete_blobs()
