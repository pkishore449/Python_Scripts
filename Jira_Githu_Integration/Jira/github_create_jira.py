from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
import os

platform=Flask(__name__)

@platform.route("/createJira", methods=['POST'])
def create_jira():
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
    if (request.path!='/create')
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
   
platform.run(host='0.0.0.0', port=5000)