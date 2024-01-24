import requests
from config import api_url

def call_api(data):
    response = requests.get(api_url, params=data)
    return response.json()
