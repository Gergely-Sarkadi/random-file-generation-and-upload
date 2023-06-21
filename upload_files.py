import os
import time
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def upload_files(num_of_files=10000, target_directory='generated_files/'):
    """Upload the previously generated files to the given Azure Blob Storage and Container"""

    load_dotenv()

    connect_str = os.getenv('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = os.getenv('AZURE_BLOB_STORAGE_CONTAINER_NAME')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    start = time.time()
    for i in range(num_of_files):
        file_path = f'./{target_directory}{i}_dummy_file.txt'
        with open(file_path, 'rb') as file_contents:
            container_client.upload_blob(name=f'testing/{i}_dummy_file.txt', data=file_contents, overwrite=True)
    end = time.time()
    print(f"Uploaded {num_of_files} files in {end - start} secs")

upload_files()
