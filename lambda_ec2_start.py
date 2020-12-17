import boto3
import os

INSTANCE_ID = os.environ['INSTANCE_ID']

def lambda_handler(event, context):

    client = boto3.client('ec2')

    response = client.start_instances(
        InstanceIds=[
            f'{INSTANCE_ID}',
        ],
    )

    print(response)