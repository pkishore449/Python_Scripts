import boto3

client=boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=['i-00a9b51e85b76939a' ]
)

response = client.terminate_instances(
    InstanceIds=['i-00a9b51e85b76939a']
)
print(response)
print("***********************************************")
response = client.delete_snapshot(
    SnapshotId='snap-00aba5777a3d6bea1'
)
print(response)











 