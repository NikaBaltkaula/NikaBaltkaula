# API URL
import requests
url = "https://reqres.in/api/users?page=2"

#send get request
response = requests.get(url)

#Display Response Content
print(response.content)
print(response.headers)