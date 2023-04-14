#!/bin/env python

import requests
#import json
import hashlib
import base64
import time
import hmac

#Account Info
AccessId ="uSzNM8LS94XIy3R47dTy"
AccessKey ="lma__%{D8{^)6~C75t6mt63R-_=63~R24Khx_Gqve]CR7qebc^~)^zy7]w3fuw^ILZjgzODM1M2ItNTcxMS00YzFjLTgwYjYtMWU5NTVkNjU1OTE1L049l8h"
Company = "lmkendallshearman"

#Request Info
httpVerb ='GET'
resourcePath = '/device/devices'
data = ''

#Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

#Get current time in milliseconds
epoch = str(int(time.time() * 1000))

#Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

#Construct signature
hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth, 'X-Version':'3'}

#Make request
response = requests.get(url, data=data, headers=headers)
#response.json()

#Print status and body of response
print('Response Status:',response.status_code)
print('Response Body:',response.content)
















