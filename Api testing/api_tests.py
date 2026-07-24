import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
response = requests.get("https://reqres.in/api/users/2",headers=headers)
json_data = response.json()
user_id= json_data["data"]["id"]
name = json_data["data"]["first_name"]
email = json_data["data"]["email"]

print(f"Id is {user_id}")
print(f"First name is {name}")
print(f"Email is {email}")

import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
response = requests.get("https://reqres.in/api/users/2",headers=headers)
json_data = response.json()

# writing assertions in python 
assert response.status_code == 200, f"Expected code is 200 got {response.status_code}"
assert json_data["data"]["first_name"]== "Janet", "First name is Janet"
assert json_data["data"]["id"]==2, "Id should be 2"
assert json_data["data"]["email"]!= "", "Email should not be empty"
print("All assertions passed")

# learning post in python requests
import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
url = "https://reqres.in/api/users/2"
body = {
    "name": "Vishnu kumar",
    "email": "Vishnukumar@gmail.com"
}
response = requests.post(url,json=body,headers=headers)
print(f"Status code is {response.status_code}")
json_data=response.json()
print(f"Created user name is {json_data["name"]}")
print(f"Created email is {json_data["email"]}")

# PUT (update the user)
import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
url = "https://reqres.in/api/users/2"
body={
    "name": "Vishnukumar Ganesh",
    "email": " Vishnuvk.ganesh@gmail.com"
}
response = requests.put(url,json=body,headers=headers)
json_data= response.json()
assert response.status_code==200
print(f"Status code is {response.status_code}")
print(f"Updated both name and email as {json_data["name"]},{json_data["email"]}")

# Delete the user
import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
url = "https://reqres.in/api/users/2"
response = requests.delete(url,headers=headers)
assert response.status_code==204
# print("User deleted succesfully")

#  Creating a reusable API test code
import requests
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
base_url = "https://reqres.in"

def get_users(user_id):
    response = requests.get(f"{base_url}/api/users/{user_id}",headers=headers)
    return response

def create_users(name,job):
    body = {"name": name,"job": job}
    response = requests.post(f"{base_url}/api/users", json=body,headers=headers)
    return response

def delete_user(user_id):
    response = requests.delete(f"{base_url}/api/users/{user_id}",headers=headers)
    return response

get_response = get_users(2)
assert get_response.status_code==200
print(f"User details are {get_response.json()["data"]["first_name"]}")

create_response = create_users("Vishnu", "QA Engineer")
assert create_response.status_code==201
new_id = create_response.json()["id"]
print(f"User created and his id is {new_id}")

delete_response = delete_user(2)
assert delete_response.status_code==204
print("User is deleted")