import requests

head = {
    'Accept': 'text/plain',
    'Authorization' : 'Bearer 47795a86c0098daa42aa15e9c38d062a42c60302e358e78ce935582f8a6d3e0f'
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

