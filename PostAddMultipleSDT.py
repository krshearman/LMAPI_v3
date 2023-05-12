#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

# Account Info
Company = "lmkendallshearman"
AccessKey = "lma_+E~WkD7pb_ydeH3_Zt(9{)N~W69a4i%im2j83b[b7{m9U+]KAm3YHuVc4)[9LZjgzODM1M2ItNTcxMS00YzFjLTgwYjYtMWU5NTVkNjU1OTE1L4wWrkh"
AccessId = "6A7cPfTTwq4KS9N9PkcZ"

# Request Info
httpVerb ='POST'
# This adds an sdt
resourcePath = '/sdt/sdts'
#data = '{"deviceId":804,"type":"ResourceSDT","sdtType":"oneTime","startDateTime":1683312240000,"endDateTime":1683315840000,"timezone":"America/Chicago","comment":""}'
# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

# # Get current time in milliseconds
# epoch = str(int(time.time() * 1000))
#
# # Concatenate Request details
# requestVars = httpVerb + epoch + data + resourcePath
#
# # Construct signature
# hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
# signature = base64.b64encode(hmac1.encode())
#
# # Construct headers
# auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
# headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make requests
#data = '{"deviceId":804,"type":"ResourceSDT","sdtType":"oneTime","startDateTime":1683312240000,"endDateTime":1683315840000,"timezone":"America/Chicago","comment":""}'

sdtlist = open('sdtupdate.csv', 'r').readlines()
#lenSDT = len(sdtlist)
response = ''

colnames = sdtlist[0].split(',')
#print(colnames)

for i in range(len(sdtlist)):
    data = ''
    dataStr = '\\n'
    #print(colnames)
    if i != 0:
        countcol = len(colnames)
        vals = sdtlist[i].split(',')

        #print(vals)
        #print(countcol)
        for j in range(countcol):
            #data = data.append()'{'+ colnames[j] + ":" +'}'
            field = colnames[j]
            x = vals[j].isdigit()
            if not x:
                value = vals[j].strip('"')
                dataStr += '\n' + '\"' + field + '\"' + ':' + '\"' + value + '\"' + ','
            else:
                value = vals[j]
                dataStr += '\n' + '\"' + field + '\"' + ':' + value + ','

    #print(dataStr[:-1])
#         data = '{'+ (json.loads(json.dumps(dataStr[:-1].strip("\n")))) + '}'
#         print(data)
#
#         # Get current time in milliseconds
#
#         epoch = str(int(time.time() * 1000))
#
#         # Concatenate Request details
#         requestVars = httpVerb + epoch + data + resourcePath
#
#         # Construct signature
#         hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
#         signature = base64.b64encode(hmac1.encode())
#
#         # Construct headers
#         auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
#         headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}
#         response = requests.post(url, data=data, headers=headers)
#
#
# # Print status and body of response
# print('Response Status:', response.status_code)
# print('Response Body:', response.content)


