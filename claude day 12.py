import requests

# url = "https://jsonplaceholder.typicode.com/todos"
# response = requests.get(url)

# print(response.status_code)
# print(response.text)


# data = response.json()
# # print(data["title"])
# print(data["completed"])
# print(type(data["completed"]))


# response = requests.get(url , params = {"userId": 1})

# comments = response.json()

# print(len(comments))
# print(comments[0]["title"])


# try :
#     response = requests.get("https://jsonplaceholder.typicode.com/todos/1" , timeout = 5)
#     response.raise_for_status()
# except requests.exceptions.RequestException:
#     print("Request Failed")
# else :
#     print(response.json())

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_todo_title(todo_id):
    url = f"{BASE_URL}/todos/{todo_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return "Not Found"
    else:
        return response.json()["title"]


print(get_todo_title(1))
print(get_todo_title(5))
print(get_todo_title(9999))