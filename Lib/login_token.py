import json
import requests

url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
post_headers = {'Content-Type': 'application/json'}
post_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "shenping",
        "password": "password@123"
    },
    "id": 1
}

re = requests.post(url, data=json.dumps(post_data), headers=post_headers)
re = json.loads(re.text)
token = re["result"]
