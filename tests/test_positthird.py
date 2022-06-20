import requests
import responses
import requests
import json
from pathlib import Path
url = "http://www.boredapi.com/api/activity?type=recreational"

def test_nr_one():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() != None

directory_name = Path('testthird.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    f = open('testthird.json')
    json_file = json.load(f)
    print(json_file)


# def test_my_api():
#     with responses.RequestsMock() as rsps:
#         rsps.add(
#             responses.GET,
#             "http://www.boredapi.com/api/activity?type=recreational",
#             status=200,
#             content_type="application/json",
#         )
#         resp = requests.get(
#             "http://www.boredapi.com/api/activity?type=recreational")
#         response = requests.get(url)
#         assert resp.status_code == 200
#         assert response.json() != None
