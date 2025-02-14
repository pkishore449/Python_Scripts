# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://pkishore449.atlassian.net/rest/api/3/issue/10011"
api=os.getenv("API_TOKEN")
email=os.getenv("EMAIL")

auth = HTTPBasicAuth(email,api)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))