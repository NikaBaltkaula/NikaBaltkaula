import requests
import responses
import requests
import json
from pathlib import Path

url = "http://www.boredapi.com/api/activity?key=5881028"
def test_nr_one():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() != None

directory_name = Path('testsecond.json')
with open(directory_name, 'r', encoding='utf-8') as f:
    f = open('testsecond.json')
    json_file = json.load(f)
    print(json_file)
    # data = json.load(f.read())
    # print(data)







# def test_my_api():
#     with responses.RequestsMock() as rsps:
#         rsps.add(
#             responses.GET,
#             "http://www.boredapi.com/api/activity?key=5881028",
#             # my_json = test2.json
#             #  json=test2.json,
#             status=200,
#             content_type="application/json",
#         )
#         resp = requests.get("http://www.boredapi.com/api/activity?key=5881028")
#         response = requests.get(url)
#         assert resp.status_code == 200
#         assert response.json() != None
  

# try:
#     response = requests.get(url)
#     status = response.status_code
#     if (status != 200 and response.headers["content-type"].strip().startswith("application/json")):
#         try:
#             json_response = response.json()
#             print(json_response)
#         except ValueError:
            
#             print('Bad Data from Server. Response content is not valid JSON')
#     elif (status != 204):
#         try:
#             print(response.text)
#         except ValueError:
#             print('Bad Data From Server. Reponse content is not valid text')
# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')


# def test_my_api():
#     with responses.RequestsMock() as rsps:
#         rsps.add(
#             responses.GET,
#             "http://www.boredapi.com/api/activity?key=5881028",
#             # my_json = test2.json
#             #  json=test2.json,
#             status=200,
#             content_type="application/json",
#         )
#         resp = requests.get("http://www.boredapi.com/api/activity?key=5881028")
#         response = requests.get(url)
#         assert resp.status_code == 200
#         assert response.json() != None


# return json.load(f)
    # lines = file.readlines()
# import os
# cwd = os.getcwd()
# print(cwd)
# # os.getcwd()
# # # Look to the path of your current working directory
# working_directory = os.getcwd()
# # # Or: file_path = os.path.join(working_directory, 'my_file.py')
# file_path = working_directory + 'test2.json'
# with open(file_path) as f:
#      data = json.load(f)
#      print(data)
# with Path("/Users/veronikabaltkaula/Desktop/bored-api-tests").open("tests.json") as f:
# with open ('/tests/tests.json') as file:
#     templates = json.load(file)
# print(templates)
# for section, commands in templates.items():
#     print(section)
# json_file_path = "/tests/tests.json"
# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())
    # print('\n'.join(commands))
    # objects = json.load()
# # Creating a dictionary
# Dictionary ={1:'activity', 2:'price'}
# Converts input dictionary into
# string and stores it in json_string
# json_string = json.dumps(Dictionary)
# print('Equivalent json string of input dictionary:',
#       json_string)
# print("        ")

# with Path("/Users/veronikabaltkaula/Desktop/bored-api-tests").open("tests.json"):
# # with open('test2.json') as f:
# #     file_content = f.read()
# #     templates = json.loads(file_content)

# # print(templates)

# # for section, commands in templates.items():
# #     print(section)
# #     print('\n'.join(commands))
# # with open('test2.json') as my_file:
# #     my_json = my_file.read()

# # my = json.loads(my_json)
# # read JSON files:
# from pathlib import Path


# def main():
#     URL = "http://www.boredapi.com/api/activity?key=5881028"
#     word = input("Enter a word:")
#     data = requests.get(url + word)
#     data = data.text
#     try:
#         data_json = json.loads(data)
#         print(data_json)
#     except json.JSONDecodeError:
#         print("Empty response")


# if __name__ == "__main__":
#     main()

#     except json.decoder.JSONDecodeError:
# print('File is empty')


# directory_name = Path('testsecond.json')
# with open(directory_name, 'r', encoding='utf-8') as f:
     
#     # try:


#    data = json.load(f.read())
# print(data)