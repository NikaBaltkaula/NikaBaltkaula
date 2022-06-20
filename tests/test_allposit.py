import requests
import responses
import requests
import json
from pathlib import Path
url = "http://www.boredapi.com/api/activity?participants=1"
def test_nr_one():
    response = requests.get(url)
    assert response.status_code != 200
    assert response.json() != None

directory_name = Path('testfourth.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    f = open('testfourth.json')
    json_file = json.load(f)
    print(json_file)