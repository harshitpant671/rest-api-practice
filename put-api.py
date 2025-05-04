import requests

head = {
    'Accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=head)

print(response.status_code)
print(response.json())


headerPut = {
    'Accept' : 'text/plain',
    'Content-Type': 'application/json'
}

putPayload = {
    "id": 15,
    "title": "Harshit David Noida",
    "dueDate": "2025-05-04T12:15:08.015Z",
    "completed": True
}


response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=headerPut, json =putPayload)
print(response.status_code)
print(response.json())

assert response.status_code == 200



