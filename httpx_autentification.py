import httpx

# Getting Access token
login_payload = {
    "email": "test@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

access_token = login_response.json()["token"]["accessToken"]

# print(f'Login status code: {login_response.status_code}')
# print(f'Ответ с JSON: {login_response.json()}')

# Autorization headers
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Status code of /api/v1/users/me
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(f'Status code of /api/v1/users/me:{me_response.status_code}')
print(f'Содержимое /api/v1/users/me: {me_response.json()}')
