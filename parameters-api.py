import requests

para = {
    'page' : 1,
    'per_page' : 3
}

url = 'https://gorest.co.in/public/v2/users'

response = requests.get(url, params=para )
print(response.json())
assert response.status_code == 200
