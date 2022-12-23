import requests
import json

URL = 'http://127.0.0.1:8000/app1/course'


data = {

    'cname':'DJango',
    'dur':20,
    'fee':5000
}

json_data = json.dumps(data)
req1  =  requests.post(url=URL,data=json_data)
data = req1.json()
print(data)