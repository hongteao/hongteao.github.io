## IAM API example application


### Install
Docker run 

### Run the app
Set the AWS config
access_key = 'Your AWS access_key'
secret_key = 'Your AWS secret_key'


## Create read policy

POST /read/

curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:{$Region}:{$AccontdId}:instance/${InstanceId}&rolename={$rolename}" http://127.0.0.1:8000/read

### Response
```json{
{
    "prediction": {
        "policy_sentry_output": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Ec2ReadInstance",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:GetConsoleOutput",
                        "ec2:GetConsoleScreenshot",
                        "ec2:GetLaunchTemplateData",
                        "ec2:GetPasswordData"
                    ],
                    "Resource": [
                        "arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}"
                    ]
                }
            ]
        }
    },
    "prediction1": {
        "policy_sentry_output": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}'''

## Create List Policy

POST /list/

curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename=test21" http://127.0.0.1:8000/list

### Response

'''json
{
    "prediction": {
        "policy_sentry_output": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Ec2ListInstance",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:DescribeInstanceAttribute"
                    ],
                    "Resource": [
                        "arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}"
                    ]
                }
            ]
        }
    },
    "prediction1": {
        "policy_sentry_output": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
'''
