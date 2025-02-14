# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://pkishore449.atlassian.net/rest/api/3/project"
api=os.getenv("API_TOKEN")
email=os.getenv("EMAIL")

auth = HTTPBasicAuth(email, api)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output=json.loads(response.text)
for i in range(len(output)):
    name=output[i]['name']
    print(name)
