import boto3

linode_obj_config = {
    "aws_access_key_id": "[access-key]",
    "aws_secret_access_key": "[secret-key]",
    "endpoint_url": "[cluster-url]",
}

client = boto3.client("s3", **linode_obj_config)
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
response = client.list_objects(Bucket='shivam')
for object in response['Contents']:
    print(object['Key'])

client.upload_file(
    Filename='shivam.txt',
    Bucket='shivam',
    Key='shivam.txt')