
from typing import Dict, Any
from fastapi import Depends, FastAPI, Form
from pydantic import BaseModel
import uvicorn
from fastapi.encoders import jsonable_encoder
import json
import json, boto3

app = FastAPI()


#Temp AWS config
global access_key
global secret_key
global iam  
global resonse
access_key = 'AKIA5JMUYENTXBY7OZFZ'
secret_key = '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'
iam = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)


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

#ARN split
    arnarray = arn.split(':', -1)


#CRUD template
    crud_template = get_crud_template_dict()
    crud_template['read'].append(arn)
    policy = write_policy_with_template(crud_template)
    policy = jsonable_encoder(policy)
    response

#Create role for trustrlelationship
    assume_role_policy_document = json.dumps({
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
    })
    response = iam.create_role(
        RoleName=rolename,
        AssumeRolePolicyDocument = assume_role_policy_document)

#Create policy in AWS
    print(json.dumps(policy, indent=4))
    response = iam.create_policy(
        PolicyName=rolename,
        PolicyDocument=json.dumps(policy, indent=4))

#Attach policy to role
    response = iam.attach_role_policy(
        RoleName=rolename,
        PolicyArn='arn:aws:iam::'+arnarray[4]+':policy/'+rolename)

#Return api callback
    return ResponseModel(prediction1={'policy_sentry_output':jsonable_encoder(assume_role_policy_document)},
    prediction={'policy_sentry_output':policy})


   


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    