import requests
url = "http://www.boredapi.com/api/activity/"

response = requests.get(url)

print(response.content)
