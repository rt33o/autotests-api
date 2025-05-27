import httpx

from tools.fakers import get_random_email

# Create user Method
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']
# print("UserId", user_id)
# print("Email", create_user_response_data)
print('Create User Status code:', create_user_response.status_code)

# Login Method
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload['password']
}

# Login Method
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']
# print('Access Token:', access_token)
print('Login Status code:', login_response.status_code)

# Patch Method
update_user_headers = {
    "Authorization": f"Bearer {access_token}"
}
update_user_payload = {

    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"

}

update_user_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{user_id}', headers=update_user_headers, json=update_user_payload
)

print('Update user data Status Code:', update_user_response.status_code)
