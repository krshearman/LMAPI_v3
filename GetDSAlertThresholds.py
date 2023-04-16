#!/bin/env python

import requests
#import json
import hashlib
import base64
import time
import hmac

# - Account Info - replace with your own values
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='GET'
deviceGroupId = 245
dsId = 1413
resourcePath = f'/device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings'
data = ''
# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

# Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make request
response = requests.get(url, data=data, headers=headers)


# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)
















