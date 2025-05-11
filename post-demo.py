from marshal import dumps

import requests
import json

base_url = 'https://reqres.in/api/users'
header = {
    'Content-Type' : 'application/json'
}

# post_payload = {
#     "name": "Kush Pant",
#     "job": "QA-Lead"
# }

json_file = open('./user.json')
json_payload = json.load(json_file)

# response = requests.post(url=base_url, headers = header, json = json_payload)
response = requests.post(url=base_url, headers = header, data=json.dumps(json_payload))

print(response.json())
print(response.text)


