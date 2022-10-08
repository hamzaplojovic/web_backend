import httpx
from termcolor import colored
import time

test_users = []

headers = {
    'accept': 'application/json',
}


for x in range(10):
    test_users.append({
    'username': f'linustorvalds{str(x)}',
    'password': 'Linus.123',
    'full_name': 'Linus Torvalds',
    'github': 'torvalds',
    'email': 'linus@linux.com',
    'age': 'string',
    'job': 'Absolute Legend',
    'role': 'string',
    'status': 'string',
    'is_active': 'string',
    'avatar': 'string',
    'languages': [
        'string',
    ],
})
    

def read_all_items():
    r = httpx.get("https://centarnit.deta.dev/users/")
    for x in range(len(r.json())):
        print(f"Approved users: {colored(str(x), 'green')}", end="\r")
        time.sleep(0.1)
    print()


def create_users():
    for x in test_users:
        r = httpx.post("https://centarnit.deta.dev/users/", json=x, headers=headers)
    return f"Users created: {colored('status: 200', 'green')}"

  
def change_users():
    for x in test_users:
        x["job"] = "Linux Kernel Head"
        r = httpx.put("https://centarnit.deta.dev/users/"+x["username"], json=x, headers=headers)
    return f"Users changed: {colored('status: 200', 'green')}"

def find_users_by_username():
    for x in test_users:
        r = httpx.get("https://centarnit.deta.dev/users/"+x["username"])
    return f"User found: {colored('status: 200', 'green')}"


def delete_users():
    for x in test_users:
        httpx.delete("https://centarnit.deta.dev/users/"+x["username"])
    return f"User deleted: {colored('status: 200', 'red')}"


usernames = "\n"+"\n".join([x["username"] for x in test_users])

print(f"Testing for: {colored(usernames, 'green')}")
print()
read_all_items()
print(create_users())
print(change_users())
print(find_users_by_username())
print(delete_users())
print()