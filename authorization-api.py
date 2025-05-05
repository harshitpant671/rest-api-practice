import requests

head = {
    'Accept': 'text/plain',
    'Authorization' : 'Bearer dsy1g1545155121515112d1f51511212f8a6d3e0fhghdgjgh54f5hgh4ggfh5'
}

body = {
    "id": 7871929,
    "name": "Siddhran Patel",
    "email": "patel_siddhran@watsica-braunsf.example",
    "gender": "female",
    "status": "inactive"
  }

url = "https://gorest.co.in/public/v2/users"

response = requests.post(url, headers=head, json=body)

print(response.status_code)
print(response.json())

getResponse = requests.get(url+'/'+str(response.json()['id']), headers=head)
print(getResponse.json())

