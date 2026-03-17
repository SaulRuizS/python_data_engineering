import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

print(r.status_code)
#200
print(r.headers['content-type'])
#'application/json; charset=utf8'
print(r.encoding)
#'utf-8'
print(r.text)
#'{"type":"User"...'
print(r.json())
#{'private_gists': 419, 'total_private_repos': 77, ...}
