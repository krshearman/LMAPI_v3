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
httpVerb ='PATCH'
# Changes a report's retention from High Flexibility to High Security
websiteId = 35
resourcePath = f"/website/websites/{websiteId}"
data = '{"disableAlerting": true, "stopMonitoring": true}'

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
response = requests.patch(url, data=data, headers=headers)


# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)
















