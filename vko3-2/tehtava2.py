from google.cloud import storage
import argparse
import os
import os.path
import time

def authenticate():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\NikoNiinimäki\keys\python-hc-319107-d532fbbadd37.json"

parser = argparse.ArgumentParser()
parser.add_argument("numlines")
args = parser.parse_args()

def download_blob(bucket_name, source_blob_name, destination_file_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


def read_file(numlines):
    while not os.path.exists(r"C:\Users\NikoNiinimäki\Viikko3\Checkpoint3\checkpoint3\vko3-2\checkpoint1"):
        time.sleep(1)

    if os.path.isfile(r"C:\Users\NikoNiinimäki\Viikko3\Checkpoint3\checkpoint3\vko3-2\checkpoint1"):
        with open("checkpoint1", "r") as file_object:

            lines = file_object.readlines()
            sorted_lines = sorted(lines, key=len)
            count = int(numlines)

            for line in sorted_lines:
                if count > 0:
                    print(line)
                    count -= 1

authenticate()
download_blob("leeroooyyjeeenkiins", "checkpoint1", "checkpoint1")
read_file(int(args.numlines))

