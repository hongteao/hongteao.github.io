
from email import policy
from typing import Dict, Any
from fastapi import Depends, FastAPI, Form
from pydantic import BaseModel
import uvicorn
from fastapi.encoders import jsonable_encoder
import json, boto3
from botocore.client import Config
config = Config(connect_timeout=15, read_timeout=15)
app = FastAPI()


#Temp AWS config
global access_key
global secret_key
access_key = ''
secret_key = ''



class ResponseModel(BaseModel):
    """
    Example: {"label":"negative", "score":0.9752}
    """
    prediction: Dict
    prediction1: Dict

@app.post("/read", response_model=ResponseModel)
async def read(rolename: str = Form(), arn: str = Form()):
    from policy_sentry.writing.template import get_crud_template_dict, get_actions_template_dict
    from policy_sentry.command.write_policy import write_policy_with_template
    
    config = Config(connect_timeout=1, read_timeout=1)

    iam = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)

#ARN split
    arnarray = arn.split(':', -1)

#CRUD template
    crud_template = get_crud_template_dict()
    crud_template['read'].append(arn)
    read_policy = write_policy_with_template(crud_template)
    read_policy = jsonable_encoder(read_policy)
    

#Create role for trustrlelationship
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": arnarray[2]+".amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    }

    response = iam.create_role(
        RoleName=rolename,
        AssumeRolePolicyDocument = json.dumps(assume_role_policy_document))

#Create policy in AWS
    response = iam.create_policy(
        PolicyName=rolename,
        PolicyDocument=json.dumps(read_policy, indent=4))

#Attach policy to role
    response = iam.attach_role_policy(
        RoleName=rolename,
        PolicyArn='arn:aws:iam::'+arnarray[4]+':policy/'+rolename)

    del response

#Return api callback
    return ResponseModel(prediction1={'policy_sentry_output':assume_role_policy_document},
    prediction={'policy_sentry_output':read_policy})


   
#--------------------------------------------------------------------------------------
@app.post("/write", response_model=ResponseModel)
async def write(rolename: str = Form(), arn: str = Form()):
    from policy_sentry.writing.template import get_crud_template_dict, get_actions_template_dict
    from policy_sentry.command.write_policy import write_policy_with_template
    import json, boto3

    iam = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)    

    config = Config(connect_timeout=1, read_timeout=1)

#ARN split
    arnarray = arn.split(':', -1)

#CRUD template
    crud_template = get_crud_template_dict()
    crud_template['write'].append(arn)
    write_policy = write_policy_with_template(crud_template)
    write_policy = jsonable_encoder(write_policy)
    del crud_template
    

#Create role for trustrlelationship
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": arnarray[2]+".amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    }

    response = iam.create_role(
        RoleName=rolename,
        AssumeRolePolicyDocument = json.dumps(assume_role_policy_document))

#Create policy in AWS
    response = iam.create_policy(
        PolicyName=rolename,
        PolicyDocument=json.dumps(write_policy, indent=4))

#Attach policy to role
    response = iam.attach_role_policy(
        RoleName=rolename,
        PolicyArn='arn:aws:iam::'+arnarray[4]+':policy/'+rolename)


#Return api callback
    return ResponseModel(prediction1={'policy_sentry_output':assume_role_policy_document},
    prediction={'policy_sentry_output':write_policy})  


#--------------------------------------------------------------------------------------
@app.post("/list", response_model=ResponseModel)
async def list(rolename: str = Form(), arn: str = Form()):
    from policy_sentry.writing.template import get_crud_template_dict, get_actions_template_dict
    from policy_sentry.command.write_policy import write_policy_with_template
    import json, boto3

    iam = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)    
    config = Config(connect_timeout=1, read_timeout=1)


#ARN split
    arnarray = arn.split(':', -1)


#CRUD template
    crud_template = get_crud_template_dict()
    crud_template['list'].append(arn)
    list_policy = write_policy_with_template(crud_template)
    list_policy = jsonable_encoder(list_policy)

    

#Create role for trustrlelationship
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": arnarray[2]+".amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    }

    response1 = iam.create_role(
        RoleName=rolename,
        AssumeRolePolicyDocument = json.dumps(assume_role_policy_document))

#Create policy in AWS
    print(json.dumps(list_policy, indent=4))
    response2 = iam.create_policy(
        PolicyName=rolename,
        PolicyDocument=json.dumps(list_policy, indent=4))

#Attach policy to role
    response3 = iam.attach_role_policy(
        RoleName=rolename,
        PolicyArn='arn:aws:iam::'+arnarray[4]+':policy/'+rolename)

#Return api callback
    return ResponseModel(prediction1={'policy_sentry_output':assume_role_policy_document},
    prediction={'policy_sentry_output':list_policy})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
