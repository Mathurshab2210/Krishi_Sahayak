import json
import requests

url='http://127.0.0.1:8000/crop_prediction'

ip_for_ml = {
    "N" : 42,
    "P" : 79,
    "K" : 85,
    "temperature" : 17.225,
    "humidity":15.25,
    "ph": 6.129
}

in_json=json.dumps(ip_for_ml)
response=requests.post(url,data=in_json)
print(response.text)