import boto3 as boto3
import os

def get_ec2_instances_by_tag_and_state(tag_key, tag_value, state, region):
    '''
    :param tag_key:
    :param tag_value:
    :param state:
    :param region:
    :return ec2.describe_instances:
    '''
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    try:
        ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        response = ec2.describe_instances(
            Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}, {'Name': 'instance-state-code', 'Values': [state]}])
    except Exception as e:
        print('An unexpected error occurred:', e)
    return response

if __name__ == '__main__':
    instances = get_ec2_instances_by_tag_and_state('k8s.io/role/master', '1', '16', 'us-east-1')
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
            for tag in instance['Tags']:
                if tag.get("Key") == 'Name':
                    print(tag['Value'])
