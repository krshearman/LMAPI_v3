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

# Request Info
httpVerb ='POST'
# This adds a DataSource instance to a device

# The deviceId below should equal the id of the device within the portal. For example, this number can be found in your
# browser's address bar. For my portal, I used this: https://lmkendallshearman.logicmonitor.com/santaba/uiv3/device/index.jsp#tree/-13-d-804.
# The device ID is the number after d-.

deviceId = 1 #enter the device ID

# Getting the datasource ID is trickier. On the resource you'd like to add instances for PingMulti, click
# "Add Monitored Instance" from the dropdown to the right of the Manage Dialogue. With Chrome dev tools open,
# follow the steps to manually add a dummy instance with an IP address. Identify the datasource ID in the headers.

dsId = 37 #enter the dsId
resourcePath = f'/device/devices/{deviceId}/devicedatasources/{dsId}/instances'
data = '{"dataSourceName":"PingMulti-","displayName":"ResourceNameTest","description":"Google IP add Test Add IP to PingMulti","wildValue":"8.8.8.8"}'

# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

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
response = requests.post(url, data=data, headers=headers)

# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)