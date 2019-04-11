"""Simple Script for ThreatGrid Hands-On Lab - Step 3.

Copyright (c) 2018-2019 Cisco and/or its affiliates.

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


import json

import requests


# Request parameters
parameters = {
    "domain": "lamp.troublerifle.bid",
    "after": "2018-07-18T21:39:13Z",
    "before": "2019-07-18T22:39:13Z",
    "api_key": "",
}

# Make the request
response = requests.get(
    "https://panacea.threatgrid.com/api/v2/iocs/feeds/domains",
    params=parameters,
)

# Check that the request was successful; raise an exception if it it wasn't
response.raise_for_status()

# Parse the response data
response_data = response.json()

# Write the parsed data to a local file
with open("step3-results.json", "w") as file:
    json.dump(response_data, file, indent=2)