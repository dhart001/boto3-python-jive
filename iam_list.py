#!/usr/bin/env python
import boto3
iam = boto3.client('iam')
#for item in iam.get_user():
#    print item.name
#    print item.UserName


try:
    response = iam.list_users()
    print response
except Exception as error:
    print error
