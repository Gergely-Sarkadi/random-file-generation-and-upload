## Testing script for generating and uploading dummy files to a Storage Account

The generate_files.py script can generate arbitrary amount and sized files with random contents.
The upload_files.py can upload theses files to a given Azure Storage Account and Container.
The delete_blobs.py can delete the previously uploaded blobs.

The repo needs a .env file with the connection string for the Storage Account and for the name of the target Container.