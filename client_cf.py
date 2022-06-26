import boto3, yaml, json

# file must in the same dir as script
template_file_location = 'resources/create-vpc-cfn.yaml'
stack_name = 'create-vpc-cfn'

# read entire file as yaml
with open(template_file_location, 'r') as content_file:
    content = yaml.load(content_file, Loader=yaml.FullLoader)

# convert yaml to json string
content = json.dumps(content)

cloud_formation_client = boto3.client('cloudformation')

print("Creating {}".format(stack_name))
response = cloud_formation_client.create_stack(
    StackName=stack_name,
    TemplateBody=content,
    # Parameters=[{ # set as necessary. Ex:
    #    'ParameterKey': 'KEY',
    #    'ParameterValue': 'VALUE'
    # }]
)