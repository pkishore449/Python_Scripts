#This code prints the PR ID & USERNAME in a GitHub Repo
import requests

url='https://api.github.com/repos/kubernetes/kubernetes/pulls'
access=requests.get(url)
output=access.json()
print('ID-----------USER')
for i in range(len(output)):
    print(output[i]["id"],"---",output[i]["user"]['login'])
    
