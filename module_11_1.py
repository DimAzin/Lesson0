import requests

r = requests.get('https://google.com/')
print(r.text)
print(r.status_code)

url = requests.Request(None, 'https://google.com/?', params={'Data1': 'data'}).prepare().url
print(url)

r = requests.get("https://en.wikipedia.org/wiki/Python")
print(r)
print(r.status_code)

r = requests.get('https://api.github.com', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])

r = requests.get('https://api.github.com/events')
r.json()
print(r.status_code)
print(r.json())

