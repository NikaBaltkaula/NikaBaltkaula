import requests
import responses
import requests
import json
from pathlib import Path
url = "http://www.boredapi.com/api/activity?minaccessibility=0&maxaccessibility=0.1"
def test_nr_one():
    response = requests.get(url)
    assert response.status_code != 200
    assert response.json() != None

directory_name = Path('testeight.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    f = open('testeight.json')
    json_file = json.load(f)
    print(json_file)