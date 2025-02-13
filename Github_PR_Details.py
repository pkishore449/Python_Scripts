#This code prints the PR ID & USERNAME in a GitHub Repo
import requests

url='https://api.github.com/repos/kubernetes/kubernetes/pulls'
access=requests.get(url)
output=access.json()
print('ID-----------USER')
for i in range(len(output)):
    print(output[i]["id"],"---",output[i]["user"]['login'])
**************************************************************************************
import requests

url='https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls'

hit_url=requests.get(url)
output=hit_url.json()
for i in range(len(output)):
    print("user id:",output[i]["id"],"-user name:",output[i]["user"]['login'],"-created date:",output[i]["created_at"])

    
