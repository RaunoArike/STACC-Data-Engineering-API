import requests
import json

baseUrl = "http://localhost:5000/"

def test_successful_get_request():
    path = "api/stocks"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 200

def test_unsuccessful_get_request():
    path = "api/stocks/shhjk"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert responseJson == "There are no S&P 500 stock names that start with SHHJK"