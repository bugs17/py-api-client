import requests
import json


endpoint = 'https://mikrotik.bugsmen.xyz/rest'
username = 'admin'
password = '12345'


# data = '{"name": "rio", "password": "123fsdgsfdg", "profile": "sewah"}'
data_hotspot = '{"server": "hotspot1", "name": "rio", "password": "rio", "profile": "test"}'
headers = {"Content-Type": "application/json"}

# req = requests.get(endpoint+'/ip/hotspot/user', auth=(username, password))

r = requests.put(endpoint+'/ip/hotspot/user', auth=(username,
                                                    password), data=data_hotspot, headers=headers)

# data_lan = 'ether5'
# data_ip = '10.55.1.1/24'

# for ip in r:
#     if data_lan == ip['interface'] and data_ip == ip['address']:
#         print('data tersedia')
#     # print('Interface : ' + ip['interface'] + '==>' + ' IP : ' + ip['address'])

# print(req.json())
