import boto3
import logging

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filters = [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    instances = ec2.instances.filter(Filters=filters)

    StoppedInstances = [instance.id for instance in instances]
    
    if len(StoppedInstances) > 0:
        startingInstance = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print startingInstance
