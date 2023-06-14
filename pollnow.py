#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

# Account Info
Company = ""
AccessKey = ""
AccessId = ""

# Generate POST endpoint URL
dsId = 5247
deviceid = 804
instanceId = 224600312
resourcePath = f'/device/devices/{deviceid}/devicedatasources/{dsId}/instances/{instanceId}/data/pollnow'
data = ''
url = f'https://{Company}.logicmonitor.com/santaba/rest{resourcePath}'  # {queryParams}


# Generate Auth
def genAuth(accessid, accesskey, endpoint, httpverb, data=''):
    epoch = str(int(time.time() * 1000))
    requestVars = httpverb + epoch + data + endpoint
    hmac1 = hmac.new(accesskey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac1.encode())
    return 'LMv1 ' + accessid + ':' + signature.decode() + ':' + epoch


auth = genAuth(AccessId, AccessKey, resourcePath, 'POST', data)
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make POST request
response = requests.post(url, data=data, headers=headers)
dataresp = json.loads(response.content)

print(response.status_code)
print(response.content)
agentId = str(dataresp['agentId'])
requestId = dataresp['requestId']

# Generate GET Endpoint URL

resourcePath = f'/device/devices/{deviceid}/devicedatasources/{dsId}/instances/{instanceId}/data/pollnow/{requestId}'
url = f'https://{Company}.logicmonitor.com/santaba/rest{resourcePath}'  # {queryParams}

# Generate Auth
auth = genAuth(AccessId, AccessKey, resourcePath, 'GET', data)

# Add AgentId to headers
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3', 'agentId': agentId}

# Wait for Generation
print("Waiting for 5 seconds")
time.sleep(5)

# Make GET request
response = requests.get(url, data=data, headers=headers)

# Print the result of poll now
print(response.status_code)
print(response.content)
