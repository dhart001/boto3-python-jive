#!/usr/bin/env python
import sys
import boto3
iam = boto3.client('iam')
for username in sys.argv[1:]:
   try:
       response = iam.delete_user(
           UserName=username)
   except Exception as error:
       print error
