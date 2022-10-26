import httpx
from termcolor import colored

HOME_URL="https://centarnit.deta.dev"


test_users = []

headers = {
    'accept': 'application/json',
}

class UserTest:
    def __init__(self, url, user_list, headers):
        self.url = url
        self.user_list = user_list
        self.headers = headers

    def test_read_all_items(self) -> str:
        r = httpx.get(self.url+"/users/")
        checked = 0
        for _ in range(len(r.json())):
            checked +=1
        return f"Approved users: {colored(str(checked), 'green')}"
    
    def test_create_users(self) -> str:
        for x in self.user_list:
            httpx.post("https://centarnit.deta.dev/users/", json=x, headers=headers)
        return f"Users created: {colored(f'status: 200', 'green')}"
    
    def test_change_users(self) -> str:
        for x in self.user_list:
            x["job"] = "Linux Kernel Head"
            httpx.put("https://centarnit.deta.dev/users/"+x["username"], json=x, headers=headers)
        return f"Users changed: {colored('status: 200', 'green')}"
    
    def test_find_users_by_username(self) -> str:
        for x in self.user_list:
            httpx.get("https://centarnit.deta.dev/users/"+x["username"])
        return f"User found: {colored('status: 200', 'green')}"

    def test_delete_users(self) -> str:
        for x in self.user_list:
            httpx.delete("https://centarnit.deta.dev/users/"+x["username"])
        return f"User deleted: {colored('status: 200', 'green')}"

        
    
for x in range(10):
    test_users.append({
    'username': f'plojovichamza{str(x)}',
    'password': 'Hamza.1234',
    'full_name': 'Hamza Plojovic',
    'github': 'hamzaplojovic',
    'email': 'hamzaplojovic@gmail.com',
    'phone_number': '+381600390707',
    'job': 'Full Stack Developer',
    'role': 'string',
    'status': 'string',
    'is_active': 'string',
    'avatar': 'string',
    'languages': [
        'string',
    ],
})

test = UserTest(HOME_URL,test_users,headers)
print(test.test_read_all_items())
print(test.test_create_users())
print(test.test_change_users())
print(test.test_find_users_by_username())
print(test.test_delete_users())