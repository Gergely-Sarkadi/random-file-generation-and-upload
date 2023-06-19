import os
import time
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def upload_files(num_of_files=10):
    """Upload the previously generated files to the given Azure Blob Storage"""

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

    # upload files
    start = time.time()
    for i in range(num_of_files):
        file_path = f'./generated_files/{i}_dummy_file.txt'
        with open(file_path, 'rb') as data:
            container_client.upload_blob(name=f'testing/{i}_dummy_file.txt', data=data, overwrite=True)
    end = time.time()
    print(f"Uploaded {num_of_files} files in {end - start} secs")

upload_files()
