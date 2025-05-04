import requests

head = {
    'Accept' : 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 150,
    "title": "Harshit David Noida",
    "dueDate": "2025-05-04T12:15:08.015Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json =request_payload)

print(response.status_code)
print(response.json())

response_body = response.json()
# print(response_body['id'])

assert response.status_code == 200
assert response_body['id'] == request_payload['id']