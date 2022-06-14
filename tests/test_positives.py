import requests
import responses

def positive_get(x):
    return x + 1

def test_answer():
    assert positive_get(3) != 5 


response = requests.get('http://www.boredapi.com/api/activity?price=0.0')
print(response.status_code)
print(response.json())