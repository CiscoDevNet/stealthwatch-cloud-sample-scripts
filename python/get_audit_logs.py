#!/usr/bin/env python

"""
This script will get audit logs for a user from Stealthwatch Cloud using the REST API.

For more information on this API, please visit:
https://developer.cisco.com/docs/stealthwatch-cloud/

 -

Script Dependencies:
    requests
Depencency Installation:
    $ pip install requests

Copyright (c) 2020, Cisco Systems, Inc. All rights reserved.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import json
import configparser
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass


# Read the config file
config = configparser.ConfigParser()
config.read("env.conf")

# Set the URL
url = "https://" + config["StealthwatchCloud"]["PORTAL_URL"] + "/api/v3/audit/log/"

# Set the authorization string
authorization = "ApiKey " + config["StealthwatchCloud"]["API_USER"] + ":" + config["StealthwatchCloud"]["API_KEY"]

# Create the request headers with authorization
request_headers = {
    "Content-Type" : "application/json",
    "Accept" : "application/json",
    "Authorization" : authorization
}

# Initialize the requests session
api_session = requests.Session()

# Get the list of audit logs for the user from Stealthwatch Cloud
response = api_session.request("GET", url, headers=request_headers, verify=False)

# If successfully able to get list of audit logs
if (response.status_code == 200):

    # Loop through the list and print each audit log message
    audit_logs = json.loads(response.content)["objects"]
    for log_message in audit_logs:
        #print(json.dumps(log_message, indent=4)) # formatted print
        print(log_message)

# If unable to fetch list of audit logs
else:
    print("An error has ocurred, while fetching audit logs, with the following code {}".format(response.status_code))


