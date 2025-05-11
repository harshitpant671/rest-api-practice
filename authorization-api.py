import requests

head = {
    'Accept': 'text/plain',
    'Authorization' : 'Bearer sdsabdhsafjhshsdfkjfhkljfjlksdfj  sjfkjsfksjdf'
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

