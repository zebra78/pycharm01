import boto3, yaml, json


def create_stack(p_template_file_location, p_stack_name):
    print('')
    # read entire file as yaml
    with open(p_template_file_location, 'r') as content_file:
        content = yaml.load(content_file, Loader=yaml.FullLoader)
    content = json.dumps(content)

    cloud_formation_client = boto3.client('cloudformation')

    print("Creating {}".format(p_stack_name))
    response = cloud_formation_client.create_stack(
        StackName=p_stack_name,
        TemplateBody=content,
    )


def delete_stack(p_stack_name):
    print("Deleting {}".format(p_stack_name))
    cloud_formation_client = boto3.client('cloudformation')
    response = cloud_formation_client.delete_stack(
        StackName=p_stack_name,
    )


def describe_stacks(p_stack_name):
    print("Deleting {}".format(p_stack_name))
    cloud_formation_client = boto3.client('cloudformation')
    response = cloud_formation_client.describe_stacks(
        StackName=p_stack_name,
    )


if __name__ == '__main__':
    template_file_location = 'resources/create-vpc-cfn.yaml'
    stack_name = 'create-vpc-cfn'
    describe_stacks(stack_name)
    # create_stack(template_file_location, stack_name)
    # delete_stack(stack_name)
# convert yaml to json string
