import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "")

# response = requests.post(BASE + "", {
#     "nama": "gege",
#     "password": "gege",
#     "username": "gege"
# })

# response = requests.put(BASE + "", {
#     "id": "57",
#     "nama": "gogo",
#     "password": "gogo",
#     "username": "gogo"
# })

# response = requests.delete(BASE, params={
#     "id": "61",
# })

print(response.json())
