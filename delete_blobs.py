import os
import time
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def delete_blobs(num_of_files=10000):
    """Delete the previously uploaded blobs"""
    load_dotenv()

    #enter credentials
    account_name = os.getenv('AZURE_BLOB_STORAGE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_BLOB_STORAGE_ACCOUNT_KEY')
    container_name = os.getenv('AZURE_BLOB_STORAGE_CONTAINER_NAME')

    #create a client to interact with blob storage
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    #use the client to connect to the container
    container_client = blob_service_client.get_container_client(container_name)

    # clean up the mess
    start = time.time()
    for i in range(num_of_files):
        container_client.delete_blob(blob=f'testing/{i}_dummy_file.txt', delete_snapshots="include")
    end = time.time()
    print(f"Deleted {num_of_files} files in {end - start} secs")

delete_blobs()
