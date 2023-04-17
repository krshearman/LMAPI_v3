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
# This adds a website
resourcePath = '/website/websites'
data = '{"groupId":"4","pollingInterval":"5","useDefaultLocationSetting":true,"useDefaultAlertSetting":true,"isInternal":false,"type":"webcheck","name":"Test041723","description":"","schema":"http","domain":"logicmonitor.com","pageLoadAlertTimeInMS":"30000","transition":"1","globalSmAlertCond":"0","overallAlertLevel":"warn","individualAlertLevel":"warn","triggerSSLStatusAlert":false,"triggerSSLExpirationAlert":false,"ignoreSSL":true,"alertExpr":"","individualSmAlertEnable":false,"testLocation":{"all":true,"smgIds":[2,4,3,5,6]},"steps":[{"useDefaultRoot":true,"url":"","HTTPVersion":"1.1","HTTPMethod":"GET","followRedirection":true,"fullpageLoad":false,"requireAuth":false,"matchType":"plain","path":"","keyword":"","invertMatch":"false","statusCode":"","type":"config","HTTPBody":"","auth":{"type":"basic","domain":"","userName":"","password":""},"postDataEditType":"raw","HTTPHeaders":""}],"properties":[]}'

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