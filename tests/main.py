import requests
import responses
import pytest
import json
import requests
from pathlib import Path
url = "http://www.boredapi.com/api/activity?key=5881028"
def test_nr_one():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() != None
directory_name = Path('test.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(data["price"])







    
# def test_my_api():
#     with responses.RequestsMock() as rsps:
#         rsps.add(
#             responses.GET,
#             "http://www.boredapi.com/api/activity?key=5881028",
# #             # my_json = test2.json
# #             #  json=test2.json,
#             status=200,
#             content_type="application/json",
#         )
#         resp = requests.get("http://www.boredapi.com/api/activity?key=5881028")
#         response = requests.get(url)
#         assert resp.status_code == 200
#         assert response.json() != None
    