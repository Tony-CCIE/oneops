from fastapi import FastAPI
import requests
import json
from Lib import login_token

url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
post_headers = {'Content-Type': 'application/json'}
post_data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "host",
        ],
        "selectInterfaces": [
            "ip"
        ]
    },
    "id": 2,
    "auth": login_token.token
}
r = requests.post(url, data=json.dumps(post_data), headers=post_headers)
# print(r.text)
r = json.loads(r.text)
r_result = r['result']
for index, item in enumerate(r_result):
    print(item['host'])



