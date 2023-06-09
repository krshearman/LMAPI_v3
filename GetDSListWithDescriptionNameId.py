#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

## Returns device/s name & id filtered on displayName


# Account Info
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='GET'
# This displays the portals first 50 DataSources in the portal by name, id, and description.
#dsId = 111
resourcePath = f'/setting/datasources/'
data = ''
queryParams = '?limit=50&fields=name,description,id'


# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath + queryParams

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

# Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make request
response = requests.get(url, data=data, headers=headers)
dataresp = json.loads(response.content)

#print(dataresp)
data = (dataresp['items'])
for i in range(len(data)):
    print(data[i]['id'])
    print(data[i]['name'])
    print(data[i]['description'])
