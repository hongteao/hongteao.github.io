## IAM API example application


### Install


### Run the app

### IAM API

### Request

### Response

### Create read
curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename=test21" http://127.0.0.1:8000/read

### Create write
curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename=test21" http://127.0.0.1:8000/read

### Create List
curl -XPOST -H "Content-Type: application/x-www-form-urlencoded" -d "arn=arn:aws:ec2:ap-northeast-2:913529381735:instance/${InstanceId}1&rolename=test21" http://127.0.0.1:8000/read
