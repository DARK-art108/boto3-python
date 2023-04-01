import boto3 
s3 = boto3.client('s3')
lst = s3.list_buckets()
for bucket in lst['Buckets']:
    print(bucket['Name'])


# s3.create_bucket(Bucket='mybucket')
# for bucket in s3.list_buckets()['Buckets']:
#     print(bucket['Name'])

# s3.delete_bucket(Bucket='mybucket')
