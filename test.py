import httpx

url = 'http://httpbin.org/headers'
headers = {'user-agent': 'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
        r = client.get(url)
print(r.json()['headers']['User-Agent'])