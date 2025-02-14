# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://pkishore449.atlassian.net/rest/api/3/issue"
api=os.getenv("API_TOKEN")
email=os.getenv("EMAIL")

auth = HTTPBasicAuth(email,api)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": { 
    "issuetype": {
      "id": "10011"
    },
    "project": {
      "key": "DPD2"
    },
    "summary": "created jira ticket using python code",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))