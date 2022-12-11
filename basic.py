import requests

endpoint = 'https://mikrotik.bugsmen.xyz/rest'
username = 'admin'
password = '12345'

r = requests.get(endpoint+'/ip/address', auth=(username, password))

print(r.json())
