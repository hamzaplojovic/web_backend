import httpx

r = httpx.post("https://centarnit.deta.dev/auth/login", data={"username":"hamzaplojovic", "password":"Hamza.1234"})
print(r.status_code)