
import http.client
import json

connection = http.client.HTTPSConnection('www.reddit.com')

headers = { 'User-Agent' : 'super moody reddit2youtube bot by /u/HakierGrzonzo' }


connection.request('GET',"/r/entitledparents/top/.json?count=20", headers)

response = connection.getresponse()
print(response.read().decode())