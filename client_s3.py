import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(bucket, file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: local file name to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    # if object_name is None:
    #     object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(bucket, file_name, p_temp_location):
    s3 = boto3.client('s3')
    local_file = p_temp_location + file_name
    try:
        s3.download_file(bucket, file_name, local_file)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def print_file(file_name):
    with open(file_name) as f:
        for line in f:
            print(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello')
    temp_location = os.getenv('TEMP')
    file_to_download = 'downloadtest.txt'
    # upload_file('umadhu1608test', '../uploadtest.txt', object_name=None)
    download_file('umadhu1608test', file_to_download, temp_location)
    print_file(temp_location+file_to_download)
