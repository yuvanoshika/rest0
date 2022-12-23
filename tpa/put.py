import requests
import json

URL = 'http://127.0.0.1:8000/app1/course/1'


data = {
    'id' : 1,
    'cname' : 'rest',
    'dur' : 150,
    'fee' : 13000
}


json_data = json.dumps(data)

req1 = requests.put(url=URL,data=json_data)

data = req1.json()

print(data)