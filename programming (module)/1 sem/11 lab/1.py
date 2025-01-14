import json

import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
data = response.json()

for user in data:
    name = user['name']
    city = user['address']['city']
    phone = user['phone']
    
    print(f'Name: {name}')
    print(f'City: {city}')
    print(f'Phone: {phone}')
    print()
