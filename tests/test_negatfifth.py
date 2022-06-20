import requests
import responses
import requests
import json
from pathlib import Path
url = "http://www.boredapi.com/api/activity?price=0.0"
def test_nr_one():
    response = requests.get(url)
    assert response.status_code != 202
    assert response.json() != None

directory_name = Path('testfifth.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    f = open('testfifth.json')
    json_file = json.load(f)
    print(json_file)