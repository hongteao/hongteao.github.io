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
}

'''
## Create List Policy

POST /list/

curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename={$rolename}" http://127.0.0.1:8000/list

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

## Create Write Policy

POST /write/

curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename={$rolename}" http://127.0.0.1:8000/wrtie

### Response

{
    "prediction": {
        "policy_sentry_output": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "MultMultNone",
                    "Effect": "Allow",
                    "Action": [
                        "iam:PassRole",
                        "ec2:CreateTags"
                    ],
                    "Resource": [
                        "*"
                    ]
                },
                {
                    "Sid": "Ec2WriteInstance",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:AssociateAddress",
                        "ec2:AssociateIamInstanceProfile",
                        "ec2:AttachClassicLinkVpc",
                        "ec2:AttachNetworkInterface",
                        "ec2:AttachVolume",
                        "ec2:CreateFleet",
                        "ec2:CreateImage",
                        "ec2:CreateInstanceExportTask",
                        "ec2:CreateNetworkInsightsPath",
                        "ec2:CreateReplaceRootVolumeTask",
                        "ec2:CreateSnapshots",
                        "ec2:DetachClassicLinkVpc",
                        "ec2:DetachNetworkInterface",
                        "ec2:DetachVolume",
                        "ec2:DisassociateIamInstanceProfile",
                        "ec2:ImportInstance",
                        "ec2:ModifyInstanceAttribute",
                        "ec2:ModifyInstanceCapacityReservationAttributes",
                        "ec2:ModifyInstanceCreditSpecification",
                        "ec2:ModifyInstanceEventStartTime",
                        "ec2:ModifyInstanceMaintenanceOptions",
                        "ec2:ModifyInstanceMetadataOptions",
                        "ec2:ModifyInstancePlacement",
                        "ec2:ModifyNetworkInterfaceAttribute",
                        "ec2:ModifyPrivateDnsNameOptions",
                        "ec2:MonitorInstances",
                        "ec2:RebootInstances",
                        "ec2:ReplaceIamInstanceProfileAssociation",
                        "ec2:ReplaceRoute",
                        "ec2:ResetInstanceAttribute",
                        "ec2:RunInstances",
                        "ec2:SendDiagnosticInterrupt",
                        "ec2:SendSpotInstanceInterruptions",
                        "ec2:StartInstances",
                        "ec2:StopInstances",
                        "ec2:TerminateInstances",
                        "ec2:UnmonitorInstances"
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
