import boto3

access_key = 'AKIA5JMUYENTXBY7OZFZ'
secret_key = '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'
iam = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)

response = iam.get_role(
    RoleName='test'
)
print(response)