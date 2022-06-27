import logging
import traceback

import boto3, yaml, json
from botocore.exceptions import ClientError

# s3 = boto3.client('s3')
# local_file = p_temp_location + file_name
# try:
#     s3.download_file(bucket, file_name, local_file)
# except ClientError as e:
#     logging.error(e)
#     return False
# return True


def create_stack(p_template_file_location, p_stack_name):
    # read entire file as yaml
    try:
        with open(p_template_file_location, 'r') as content_file:
            content = yaml.load(content_file, Loader=yaml.FullLoader)
        content = json.dumps(content)

        cloud_formation_client = boto3.client('cloudformation')

        print("Creating {}".format(p_stack_name))
        response = cloud_formation_client.create_stack(
            StackName=p_stack_name,
            TemplateBody=content,
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_stack(p_stack_name):
    try:
        print("Deleting {}".format(p_stack_name))
        cloud_formation_client = boto3.client('cloudformation')
        response = cloud_formation_client.delete_stack(
            StackName=p_stack_name,
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


def describe_stacks(p_stack_name):
    try:
        print("Deleting {}".format(p_stack_name))
        cloud_formation_client = boto3.client('cloudformation')
        response = cloud_formation_client.describe_stacks(
            StackName=p_stack_name,
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    try:
        # template_file_location = 'resources/create-vpc-cfn.yaml'
        template_file_location = 'resources/create-bastion-cfn.yaml'
        # stack_name = 'create-vpc-cfn'
        stack_name = 'create-bastion-cfn'
        # describe_stacks(stack_name)
        create_stack(template_file_location, stack_name)
        # delete_stack(stack_name)
        # convert yaml to json string
    except:
        traceback.print_exc()