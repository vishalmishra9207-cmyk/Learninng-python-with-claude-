import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# response = requests.get(f"{BASE_URL}/users")
# users = response.json()

# print(len(users))

# for user in users:
#     print(f"User NAME: {user['name']}, Email: {user['email']}")


# first_user = users[0]
# print(first_user["address"]["city"])
# print(first_user["company"]["name"])


def fetch_json(url , params = None):
    try :
        response = requests.get(url , params = params, timeout = 5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else :
        return response.json()

users = fetch_json(f"{BASE_URL}/users")
print(len(users))

print(fetch_json(f"{BASE_URL}/userss"))


albums = fetch_json(f"{BASE_URL}/posts", params={"userId": 1})

if albums is None:
    print("Could not fetch albums")
else:
    print(len(albums))
    for album in albums[:3]:
        print(album["title"])



users = fetch_json(f"{BASE_URL}/users")

short_users = []

for user in users:
    short_users.append({
        "user_name" : user["name"] ,
        "email" : user["email"] ,
        "city" : user["address"]["city"]
    })

print(short_users)