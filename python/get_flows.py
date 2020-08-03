#!/usr/bin/env python

"""
This script will get flows from Stealthwatch Cloud using the REST API.

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
import datetime
import configparser
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass


# Read the config file
config = configparser.ConfigParser()
config.read("env.conf")

# Set the URL
url = "https://" + config["StealthwatchCloud"]["PORTAL_URL"] + "/api/v3/snapshots/session-data/"

# Set the authorization string
authorization = "ApiKey " + config["StealthwatchCloud"]["API_USER"] + ":" + config["StealthwatchCloud"]["API_KEY"]

# Create the request headers with authorization
request_headers = {
    "Content-Type" : "application/json",
    "Accept" : "application/json",
    "Authorization" : authorization
}

# Set the timestamps for the filters, in the correct format, for last 60 minutes
end_datetime = datetime.datetime.utcnow()
start_datetime = end_datetime - datetime.timedelta(minutes=60)
end_timestamp = end_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
start_timestamp = start_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

request_parameters = {
    "start_timestamp_utc__gte" : start_timestamp,
    "start_timestamp_utc__lt" : end_timestamp
}

# Initialize the requests session
api_session = requests.Session()

# Get the list of flows from Stealthwatch Cloud
response = api_session.request("GET", url, headers=request_headers, params=request_parameters, verify=False)

# If successfully able to get list of flows
if (response.status_code == 200):

    # Loop through the list and print each flows
    flows = json.loads(response.content)["objects"]
    for flow in flows:
        #print(json.dumps(flow, indent=4)) # formatted print
        print(flow)

# If unable to fetch list of alerts
else:
    print("An error has ocurred, while fetching flows, with the following code {}".format(response.status_code))


