import requests

API_URL = "https://api-ad2bfb4d-4efc3229-dku.eu-west-3.app.dataiku.io/public/api/v1/cc_f/sc/run"

def call_api(data):
    response = requests.get(API_URL, params=data)
    return response.json()
