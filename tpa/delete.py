import requests
import json


URL = 'http://127.0.0.1:8000/app1/course/1'


data = {
    'id' : 4,
}



json_data = json.dumps(data)

req1 = requests.delete(url=URL,data=json_data)

data = req1.json()

print(data)