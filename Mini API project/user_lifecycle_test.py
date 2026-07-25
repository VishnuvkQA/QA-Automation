import requests
base_url = "https://reqres.in"
headers = {
    "x-api-key": "free_user_3GrgdFJI6qoJlHygcGI4uya5IwA"
}
# Creating a user
body = {
    "name": "Vishnukumar",
    "job": "QA Engineer"
}
response = requests.post(f"{base_url}/api/users", json = body,headers=headers)
assert response.status_code==201, f"Expected code is 201, but we got {response.status_code}"
json_data = response.json()
user_id = json_data["id"]
print(f"Created a user with id {user_id}")

# Verifying the user already in the website using GET
response = requests.get(f"{base_url}/api/users/2",headers=headers)
json_data = response.json()
assert response.status_code==200, f"Expected 200 but we got {response.status_code}"
assert json_data["data"]["first_name"] == "Janet", f"Expected first name is Janet but we got {json_data["data"]["first_name"]}"
print(f"Verified user  {json_data["data"]["first_name"]}")

# Updating the existing user
body = {
    "name": "Jimmy Janet",
    "job" : "Senior QA Engineer"
}
response = requests.put(f"{base_url}/api/user/", json=body,headers=headers)
json_data = response.json()
assert response.status_code==200, f"Expected code is 200 but we got {response.status_code}"
print(f"Name has been updated to {json_data["name"]}")
print(f"Job has been updated to {json_data["job"]}")    

# Deleting the user
response = requests.delete(f"{base_url}/api/users/2",headers=headers)
assert response.status_code==204, f"Expected status code is 204 but we got {response.status_code}"
print(f"User has been deleted successfully")

# Verifying the deleted user
response = requests.get(f"{base_url}/api/users/99",headers=headers)
assert response.status_code==404, f"Expected code is 404 but we got {response.status_code}"
print(f"Verified: User not found {response.status_code}")

print("All Lifecycle tests passed ")