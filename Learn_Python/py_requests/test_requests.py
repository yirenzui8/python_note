import requests
import json
#-*-coding:utf-8-*-
# payload = json.dumps({"function": "GetRaAccountInfo","deviceId": "708101160500000147"})
payload = json.dumps({"Request":{"method":"getAccount","parameters":{"accountId":["708101160500000170","708101160500000170"]}}})

# r = requests.post("http://account.baustem.net:8080/account",data=payload)
# r = requests.post("http://account.baustem.net:8080/cfg",data=payload)
r = requests.get("http://192.168.5.1")
print r.text
# print r.json()

# print r.status_code