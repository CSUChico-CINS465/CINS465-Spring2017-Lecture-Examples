import requests

for i in range(150):
    r = requests.get('http://localhost:5000/add/2/3')
