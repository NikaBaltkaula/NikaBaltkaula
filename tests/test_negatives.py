import requests
import responses
import requests
import json
from responses import json_params_matcher, matchers
url = "http://www.boredapi.com/api/activity"


def test_nr_one():
    response = requests.get(url)
    assert response.status_code != 206
    assert response.json() != None
# response = requests.get(url)
# print(response)

my_json = { "activity": "Learn Morse code",
    "type": "education",
    "participants": 1,
    "price": 0,
    "link": "https://en.wikipedia.org/wiki/Morse_code",
    "key": "3646173",
    "accessibility": 0}
def test_my_api():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "http://www.boredapi.com/api/activity",
        json=my_json,
        status=200,
            content_type="application/json",
        )
        resp = requests.get("http://www.boredapi.com/api/activity")
        response = requests.get(url)
        method = response.json()
        print(type(method["price"]))
        assert resp.status_code == 200
        assert response.json() != None
        assert method["price"] == 0
        print(my_json)
        
